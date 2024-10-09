from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.urls import reverse
from src.core.forms import GalleryImageFormSet
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Page, MainPage, SEOMixin
from .forms import PageForm, GalleryImageFormSet, MainPageForm, ContactsFormSet
from django.db import transaction
from src.core.models import GalleryImage, Gallery
from src.core.forms import SEOMixinForm
from django.db import models
from src.users.models import User

from django.contrib.auth.decorators import login_required

from ..movies.models import Movie
from ..showtimes.models import Ticket


from django.db.models import Count
from django.utils import timezone
from datetime import timedelta


@login_required
def admin_dashboard(request):
    # users information
    total_users = User.objects.count()
    male_users = User.objects.filter(gender='M').count()
    female_users = User.objects.filter(gender='F').count()
    users_by_city = User.objects.values('city').annotate(count=Count('id')).order_by('-count')

    # tickets
    total_tickets = Ticket.objects.count()

    # most popular movie last month
    one_month_ago = timezone.now() - timedelta(days=30)
    most_popular_movies = (
        Movie.objects
        .annotate(ticket_count=Count('showtime__ticket', filter=models.Q(showtime__show_time__gte=one_month_ago)))
        .order_by('-ticket_count')[:5]  # 5 movies
    )

    # data for diagram
    movie_names = [movie.name_uk for movie in most_popular_movies]
    tickets_sold = [movie.ticket_count for movie in most_popular_movies]

    context = {
        'total_users': total_users,
        'male_users': male_users,
        'female_users': female_users,
        'users_by_city': users_by_city,
        'total_tickets': total_tickets,
        'movie_names': movie_names,
        'tickets_sold': tickets_sold,
    }

    return render(request, 'admin/pages/admin_dashboard.html', context)


@login_required
@transaction.atomic
def add_page(request):
    if request.method == 'POST':
        form = PageForm(request.POST, request.FILES)
        formset = GalleryImageFormSet(request.POST, request.FILES)

        if form.is_valid() and formset.is_valid():
            page = form.save(commit=False)

            # save main img
            main_image_id = form.cleaned_data['main_image']
            if main_image_id:
                try:
                    main_image = GalleryImage.objects.get(pk=main_image_id.id)
                    page.main_image = main_image
                except GalleryImage.DoesNotExist:
                    messages.error(request, 'Image not found')
                    return render(request, 'admin/pages/add_page.html',
                                  {'form': form, 'formset': formset})

            gallery = Gallery.objects.create()
            page.gallery = gallery
            page.save()

            formset.instance = gallery
            formset.save(commit=True)

            messages.success(request, 'Page successfully added')
            return redirect('pages_list')
        else:
            messages.error(request, 'Form or formset not valid')
    else:
        form = PageForm()
        formset = GalleryImageFormSet()

    return render(request, 'admin/pages/add_page.html', {'form': form, 'formset': formset})


# view for get template for success page
@login_required
def page_success(request):
    return render(request, 'admin/pages/page_success.html')



# view for getting list of all pages
@login_required
def get_page_list(request):
    if request.method == 'GET':
        page_list = Page.objects.all()

        pages_data = []
        for page in page_list:
            page_data = {
                'id': page.id,
                'name': page.name,
            }
            pages_data.append(page_data)

        return JsonResponse({'pages_list': pages_data})
    return JsonResponse({'error': 'Invalid request method'}, status=400)


@login_required
def page_list_view(request):
    pages = Page.objects.all()
    return render(request, 'admin/pages/pages_list.html', {'pages': pages})


@login_required
@transaction.atomic
def edit_page(request, page_id):
    page = get_object_or_404(Page, id=page_id)
    gallery = page.gallery

    if request.method == 'POST':
        form = PageForm(request.POST, request.FILES, instance=page)
        formset = GalleryImageFormSet(request.POST, request.FILES, instance=gallery)

        if form.is_valid() and formset.is_valid():
            page = form.save(commit=False)

            # save main img
            new_main_image_id = form.cleaned_data.get('main_image')
            if new_main_image_id:
                try:
                    new_main_image = GalleryImage.objects.get(pk=new_main_image_id.id)
                    if page.main_image != new_main_image:
                        page.main_image = new_main_image
                except GalleryImage.DoesNotExist:
                    messages.error(request, 'Image not found')
                    return render(request, 'admin/pages/edit_page.html',
                                  {'form': form, 'formset': formset, 'page': page, 'gallery': gallery})
            else:
                page.main_image = page.main_image

            if not gallery:
                gallery = Gallery.objects.create()
                page.gallery = gallery

            page.save()
            formset.instance = gallery
            formset.save()

            messages.success(request, 'Page edited successfully')
            return redirect('all_page_list')
        else:
            messages.error(request, 'Form or formset not valid')
    else:
        form = PageForm(instance=page)
        formset = GalleryImageFormSet(instance=gallery)

    return render(request, 'admin/pages/edit_page.html',
                  {'form': form, 'formset': formset, 'page': page})


# view for delete page from DB
@login_required
def delete_page(request, page_id):
    page = get_object_or_404(Page, id=page_id)

    if request.method == 'POST':
        page.delete()
        return redirect('pages_list')

    return render(request, 'admin/pages/confirm_delete_page.html', {'page': page})


@login_required
def main_page(request):
    main_page_instance = MainPage.objects.first()

    if request.method == 'POST':
        form = MainPageForm(request.POST, request.FILES, instance=main_page_instance)

        if form.is_valid():
            main_page = form.save(commit=False)
            main_page.save()
            messages.success(request, 'Page edited successfully')
            return redirect('pages_list')
        else:
            messages.error(request, 'Form or formset not valid')
    else:
        form = MainPageForm(instance=main_page_instance)

    return render(request, 'admin/main_page/main_page_admin.html', {'form': form})


@login_required
@transaction.atomic
def contacts_view(request):
    seo_instance, created = SEOMixin.objects.get_or_create(id=1)

    if request.method == 'POST':
        seo_form = SEOMixinForm(request.POST, instance=seo_instance)
        contact_formset = ContactsFormSet(request.POST, request.FILES, instance=seo_instance)

        if seo_form.is_valid() and contact_formset.is_valid():
            seo = seo_form.save()

            try:
                # Save the contacts formset
                instances = contact_formset.save(commit=False)
                for instance in instances:
                    instance.seo = seo  # Link the SEO instance to each contact
                    instance.save()
                for instance in contact_formset.deleted_objects:
                    instance.delete()
                contact_formset.save_m2m()

                messages.success(request, 'Contact edited successfully')
                return redirect('pages_list')
            except Exception as e:
                messages.error(request, 'There was an error while saving contacts')
        else:
            messages.error(request, 'Form or formset is invalid')
    else:
        seo_form = SEOMixinForm(instance=seo_instance)
        contact_formset = ContactsFormSet(instance=seo_instance)

    return render(request, 'admin/contacts/add_contacts.html', {
        'seo_form': seo_form,
        'contact_formset': contact_formset,
    })


@login_required
def pages_list(request):
    context = {
        'pages_list': [
            {'name': 'Main page', 'edit_url': reverse('main_page')},
            {'name': 'All pages', 'edit_url': reverse('all_page_list')},
            {'name': 'Contacts page', 'edit_url': reverse('add_contacts')}
        ]
    }
    return render(request, 'admin/pages.html', context)




