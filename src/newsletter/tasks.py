from celery import shared_task
from django.core.mail import send_mail
from .models import EmailCampaign
from src.users.models import User


@shared_task
def send_email_campaign(campaign_id):
    try:
        campaign = EmailCampaign.objects.get(id=campaign_id)
        if campaign.send_to_all:
            user_emails = list(User.objects.values_list('email', flat=True))
        else:
            user_emails = list(User.objects.filter(id__in=campaign.selected_users_ids).values_list('email', flat=True))

        total_emails = len(user_emails)
        sent_count = 0

        for email in user_emails:
            send_mail(
                subject=campaign.name,
                message='',
                html_message=campaign.email_template.description,
                from_email='kinocmstestmail@gmail.com',
                recipient_list=[email]
            )
            sent_count += 1
            campaign.progress = int((sent_count / total_emails) * 100)
            campaign.sent_count = sent_count
            campaign.save(update_fields=['progress', 'sent_count'])

        campaign.status = 'sent'
        campaign.save()

    except Exception as e:
        raise e
