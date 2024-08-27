from .models import EmailTemplate
from src.users.models import User
from django.core.paginator import Paginator

from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .forms import EmailCampaignForm
from .models import EmailCampaign
from .tasks import send_email_campaign

import logging

logger = logging.getLogger(__name__)


def email_campaign_view(request):
    if request.method == 'POST':
        form = EmailCampaignForm(request.POST, request.FILES)
        logger.debug(f"POST data: {request.POST}")
        logger.debug(f"FILES data: {request.FILES}")
        if not form.is_valid():
            logger.debug(f"Form errors: {form.errors}")
            return JsonResponse({'status': 'error', 'message': 'Форма містить помилки.'}, status=400)

        try:
            if 'selected_template' in request.POST:
                template_id = request.POST.get('selected_template')
                email_campaign = EmailCampaign.objects.get(id=template_id)
                email_template = email_campaign.email_template

                logger.debug(f"Selected template ID: {template_id}")

                campaign = form.save(commit=False)
                campaign.name = email_template.name
                campaign.email_template = email_template
                campaign.send_to_all = email_campaign.send_to_all

                if campaign.send_to_all:
                    all_users = User.objects.values_list('id', flat=True)
                    campaign.selected_users_ids = list(all_users)
                else:
                    campaign.selected_users_ids = email_campaign.selected_users_ids

            elif 'html_file' in request.FILES:
                html_file = request.FILES['html_file']
                file_name_without_extension = '.'.join(html_file.name.split('.')[:-1])
                email_template = EmailTemplate.objects.create(
                    name=file_name_without_extension,
                    description=html_file.read().decode('utf-8')
                )
                campaign_name = file_name_without_extension

                campaign = form.save(commit=False)
                campaign.name = campaign_name
                campaign.email_template = email_template
                campaign.send_to_all = (form.cleaned_data['users'] == 'all')

                if campaign.send_to_all:
                    all_users = User.objects.values_list('id', flat=True)
                    campaign.selected_users_ids = list(all_users)
                else:
                    selected_users_str = request.POST.get('selected_users')
                    selected_users = [int(user_id) for user_id in selected_users_str.split(',')]
                    campaign.selected_users_ids = selected_users
            else:
                return JsonResponse(
                    {'status': 'error', 'message': 'HTML файл не завантажений і шаблон не вибраний.'}, status=400)

            campaign.save()

            send_email_campaign.delay(campaign.id)

            return JsonResponse({'status': 'success', 'campaign_id': campaign.id,
                                 'message': 'Кампанія розпочата успішно!'})

        except EmailTemplate.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Шаблон не знайдено.'}, status=404)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    else:
        form = EmailCampaignForm()
        latest_campaigns = EmailCampaign.objects.all().order_by('-created_at')[:5]
        users_list = User.objects.all().order_by('id')
        paginator = Paginator(users_list, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    context = {
        'form': form,
        'latest_campaigns': latest_campaigns,
        'template_name': '',
        'page_obj': page_obj,
        'email_count': 0,
        'progress': 0
    }

    return render(request, 'admin/email_newsletter.html', context)


def save_selected_users(request):
    if request.method == 'POST':
        selected_users = request.POST.getlist('selected_users')
        request.session['selected_users'] = selected_users
        return redirect('email_campaign')


def delete_template(request, template_id):
    template = get_object_or_404(EmailCampaign, id=template_id)
    template.delete()
    return redirect('email_campaign')


def check_campaign_progress(request, campaign_id):
    campaign = EmailCampaign.objects.get(id=campaign_id)
    logger.info(f"Перевірка прогресу кампанії: {campaign_id}, поточний прогрес: {campaign.progress}%")
    data = {
        'progress': campaign.progress,
        'sent_count': campaign.sent_count,
    }
    return JsonResponse(data)
