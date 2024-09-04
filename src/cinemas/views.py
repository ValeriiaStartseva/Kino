from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from .models import Hall, Cinema
from .forms import CinemaForm, GalleryImageFormSet, HallForm
from src.core.models import Gallery, GalleryImage
from django.contrib import messages
from django.http import JsonResponse


# view for adding new cinema to DB
@transaction.atomic
def add_cinema(request):
    if request.method == "POST":
        form = CinemaForm(request.POST, request.FILES)
        formset = GalleryImageFormSet(request.POST, request.FILES)

        if form.is_valid() and formset.is_valid():
            cinema = form.save(commit=False)

            # save main image
            main_image_id = form.cleaned_data['main_image']
            if main_image_id:
                try:
                    main_image = GalleryImage.objects.get(pk=main_image_id.id)
                    cinema.main_image = main_image
                except GalleryImage.DoesNotExist:
                    messages.error(request, 'Картинка не існує.')
                    return render(request, 'admin/add_cinema.html',
                                  {'form': form, 'formset': formset})

            # save img  banner - logo here
            logo_id = form.cleaned_data['logo']
            if logo_id:
                try:
                    logo = GalleryImage.objects.get(pk=logo_id.id)
                    cinema.logo = logo
                except GalleryImage.DoesNotExist:
                    messages.error(request, 'Image does not exist.')
                    return render(request, 'admin/add_cinema.html',
                                  {'form': form, 'formset': formset})

            # Create gallery
            gallery = Gallery.objects.create()
            cinema.gallery = gallery
            cinema.save()

            formset.instance = gallery
            formset.save()

            messages.success(request, 'Кінотеатр успішно додано.')
            return redirect('add_hall', cinema_id=cinema.id)  # Redirect to a page of creating hall

    else:
        form = CinemaForm()
        formset = GalleryImageFormSet()

    return render(request, 'admin/add_cinema.html', {'form': form, 'formset': formset})


# view for edit cinema model
@login_required
@transaction.atomic
def edit_cinema(request, cinema_id):

    cinema = get_object_or_404(Cinema, id=cinema_id)
    gallery = cinema.gallery
    halls = Hall.objects.filter(cinema_hall=cinema)

    if request.method == "POST":

        form = CinemaForm(request.POST, request.FILES, instance=cinema)
        formset = GalleryImageFormSet(request.POST, request.FILES, instance=gallery)

        if form.is_valid() and formset.is_valid():

            cinema = form.save(commit=False)

            # edit or save main img
            new_main_image_id = form.cleaned_data.get('main_image')

            if new_main_image_id:
                try:
                    new_main_image = GalleryImage.objects.get(pk=new_main_image_id.id)
                    if cinema.main_image != new_main_image:
                        cinema.main_image = new_main_image

                except GalleryImage.DoesNotExist:
                    messages.error(request, 'Картинка не існує.')
                    return render(request, 'admin/add_cinema.html', {'form': form, 'formset': formset})
            else:
                cinema.main_image = cinema.main_image

            # edit or save new banner - logo here
            new_logo_id = form.cleaned_data.get('logo')
            if new_logo_id:
                try:
                    new_logo = GalleryImage.objects.get(pk=new_logo_id.id)
                    if cinema.logo != new_logo:
                        cinema.logo = new_logo

                except GalleryImage.DoesNotExist:

                    messages.error(request, 'Image does not exist.')
                    return render(request, 'admin/add_cinema.html',
                                  {'form': form, 'formset': formset})
            else:
                cinema.logo = cinema.logo

            # gallery
            if not gallery:
                gallery = Gallery.objects.create()
                cinema.gallery = gallery

            cinema.save()

            formset.instance = gallery
            formset.save()

            messages.success(request, 'Cinema added successfully.')
            return redirect('cinema_list')


    else:
        form = CinemaForm(instance=cinema)
        formset = GalleryImageFormSet(instance=gallery)

    return render(request, 'admin/edit_cinema.html',
                  {'form': form, 'formset': formset, 'cinema': cinema, 'halls': halls})


# view for getting all cinemas
@login_required
def get_list_cinema(request):
    if request.method == 'GET':
        cinema_list = Cinema.objects.all()

        cinemas_data = []
        for cinema in cinema_list:
            cinema_data = {
                'id': cinema.id,
                'name': cinema.name,
            }
            cinemas_data.append(cinema_data)

        return JsonResponse({'cinemas_list': cinemas_data})
    return JsonResponse({'error': 'Invalid request method'}, status=400)


# view for page with table of all cinemas
@login_required
def cinema_list_view(request):
    cinemas = Cinema.objects.all()
    return render(request, 'admin/cinemas_list.html', {'cinemas': cinemas})


# view for get template for success cinema page
@login_required
def cinema_success(request):
    return render(request, 'admin/cinema_success.html')


# view for delete cinema from DB
@login_required
def delete_cinema(request, cinema_id):
    cinema = get_object_or_404(Cinema, id=cinema_id)

    if request.method == 'POST':
        cinema.delete()
        return redirect('cinema_list')

    return render(request, 'admin/delete_cinema_confirm.html', {'cinema': cinema})


# view for add new hall to the DB
@login_required
@transaction.atomic
def add_hall(request, cinema_id):

    cinema = get_object_or_404(Cinema, id=cinema_id)

    if request.method == "POST":
        form = HallForm(request.POST, request.FILES)
        formset = GalleryImageFormSet(request.POST, request.FILES)

        if form.is_valid() and formset.is_valid():
            try:
                hall = form.save(commit=False)
                hall.cinema_hall = cinema  # Зв'язок залу з кінотеатром

                # Save main img
                main_image_id = form.cleaned_data['main_image']
                if main_image_id:
                    try:
                        main_image = GalleryImage.objects.get(pk=main_image_id.id)
                        hall.main_image = main_image
                    except GalleryImage.DoesNotExist:
                        messages.error(request, 'Картинка не існує.')
                        return render(request, 'admin/add_hall.html',
                                      {'form': form, 'formset': formset})

                # Save schema of hall
                schema_picture_id = form.cleaned_data['schema_picture']
                if schema_picture_id:
                    try:
                        schema_picture = GalleryImage.objects.get(pk=schema_picture_id.id)
                        hall.schema_picture = schema_picture
                    except GalleryImage.DoesNotExist:
                        messages.error(request, 'Картинка не існує.')
                        return render(request, 'admin/add_hall.html',
                                      {'form': form, 'formset': formset})

                # gallery
                gallery = Gallery.objects.create()
                hall.gallery = gallery
                hall.save()

                formset.instance = gallery
                formset.save()

                messages.success(request, 'Зал успішно додано.')
                return redirect('edit_cinema', cinema_id=cinema.id)  # Redirect to the cinema edit page
            except Exception as e:

                messages.error(request, f"An error occurred: {e}")


    else:
        form = HallForm()
        formset = GalleryImageFormSet()

    return render(request, 'admin/add_hall.html',
                  {'form': form, 'formset': formset, 'cinema': cinema})


# view for edit hall model
@login_required
@transaction.atomic
def edit_hall(request, hall_id):

    hall = get_object_or_404(Hall, id=hall_id)
    cinema = hall.cinema_hall_id
    gallery = hall.gallery


    if request.method == "POST":

        form = HallForm(request.POST, request.FILES, instance=hall)
        formset = GalleryImageFormSet(request.POST, request.FILES, instance=gallery)

        if form.is_valid() and formset.is_valid():

            hall = form.save(commit=False)

            new_main_image_id = form.cleaned_data.get('main_image')
            if new_main_image_id:
                try:
                    new_main_image = GalleryImage.objects.get(pk=new_main_image_id.id)
                    if hall.main_image != new_main_image:
                        hall.main_image = new_main_image

                except GalleryImage.DoesNotExist:

                    messages.error(request, 'Image not found')
                    return render(request, 'admin/add_cinema.html',
                                  {'form': form, 'formset': formset})
            else:
                hall.main_image = hall.main_image


            new_schema_id = form.cleaned_data.get('schema_picture')
            if new_schema_id:
                try:
                    new_schema = GalleryImage.objects.get(pk=new_schema_id.id)
                    if hall.schema_picture != new_schema:
                        hall.schema_picture = new_schema

                except GalleryImage.DoesNotExist:

                    messages.error(request, 'Image does not exist')
                    return render(request, 'admin/add_cinema.html',
                                  {'form': form, 'formset': formset})
            else:
                hall.schema = hall.schema

            if not gallery:
                gallery = Gallery.objects.create()
                hall.gallery = gallery

            hall.save()

            formset.instance = gallery
            formset.save()

            messages.success(request, 'Hall added successfully!')
            return redirect('edit_cinema', cinema_id=cinema)  # Redirect to the cinema edit page

    else:
        form = HallForm(instance=hall)
        formset = GalleryImageFormSet(instance=gallery)

    return render(request, 'admin/edit_hall.html', {'form': form,
                                                    'formset': formset, 'hall': hall})


# view for delete hall from the DB
@login_required
def delete_hall(request, hall_id):
    hall = get_object_or_404(Hall, id=hall_id)
    cinema = hall.cinema_hall_id
    if request.method == 'POST':
        hall.delete()
        return redirect('edit_cinema', cinema_id=cinema)

    return render(request, 'admin/delete_hall_confirm.html', {'hall': hall, 'cinema': cinema})

@login_required
def cinema_detail(request):
    halls = Hall.objects.all()
    return render(request, 'admin/add_cinema.html', {'halls': halls})
