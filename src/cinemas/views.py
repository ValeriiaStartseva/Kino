from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from .models import Hall, Cinema
from .forms import CinemaForm, GalleryImageFormSet, HallForm
from src.core.models import Gallery, GalleryImage
from django.contrib import messages
from django.http import JsonResponse
import logging

logger = logging.getLogger(__name__)


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
                    return render(request, 'admin/add_cinema.html', {'form': form, 'formset': formset})

            # save img  banner - logo here
            logo_id = form.cleaned_data['logo']
            if logo_id:
                try:
                    logo = GalleryImage.objects.get(pk=logo_id.id)
                    cinema.logo = logo
                except GalleryImage.DoesNotExist:
                    messages.error(request, 'Картинка не існує.')
                    return render(request, 'admin/add_cinema.html', {'form': form, 'formset': formset})

            # Create gallery
            gallery = Gallery.objects.create()
            cinema.gallery = gallery
            cinema.save()

            formset.instance = gallery
            formset.save()

            messages.success(request, 'Кінотеатр успішно додано.')
            return redirect('add_hall', cinema_id=cinema.id)  # Redirect to a page of creating hall
        else:
            print("Form or formset is not valid")
            print(form.errors)
            print(formset.errors)

    else:
        form = CinemaForm()
        formset = GalleryImageFormSet()

    return render(request, 'admin/add_cinema.html', {'form': form, 'formset': formset})


# view for edit cinema model
@transaction.atomic
def edit_cinema(request, cinema_id):
    logger.info("Started editing cinema with ID %s", cinema_id)
    cinema = get_object_or_404(Cinema, id=cinema_id)
    gallery = cinema.gallery
    halls = Hall.objects.filter(cinema_hall=cinema)
    logger.info("Loaded cinema: %s, gallery: %s, halls: %s", cinema, gallery, halls)

    if request.method == "POST":
        logger.info("Processing POST request")
        form = CinemaForm(request.POST, request.FILES, instance=cinema)
        formset = GalleryImageFormSet(request.POST, request.FILES, instance=gallery)

        if form.is_valid() and formset.is_valid():
            logger.info("Forms are valid")
            cinema = form.save(commit=False)

            # resave or save main img
            new_main_image_id = form.cleaned_data.get('main_image')
            if new_main_image_id:
                try:
                    new_main_image = GalleryImage.objects.get(pk=new_main_image_id.id)
                    if cinema.main_image != new_main_image:
                        cinema.main_image = new_main_image
                    logger.info("Updated main image: %s", new_main_image)
                except GalleryImage.DoesNotExist:
                    logger.error("Main image does not exist")
                    messages.error(request, 'Картинка не існує.')
                    return render(request, 'admin/add_cinema.html', {'form': form, 'formset': formset})
            else:
                cinema.main_image = cinema.main_image
                logger.info("Retained existing main image")

            # resave or save new banner - logo here
            new_logo_id = form.cleaned_data.get('logo')
            if new_logo_id:
                try:
                    new_logo = GalleryImage.objects.get(pk=new_logo_id.id)
                    if cinema.logo != new_logo:
                        cinema.logo = new_logo
                    logger.info("Updated logo: %s", new_logo)
                except GalleryImage.DoesNotExist:
                    logger.error("Logo does not exist")
                    messages.error(request, 'Картинка не існує.')
                    return render(request, 'admin/add_cinema.html', {'form': form, 'formset': formset})
            else:
                cinema.logo = cinema.logo
                logger.info("Retained existing main image")

            # gallery
            if not gallery:
                gallery = Gallery.objects.create()
                cinema.gallery = gallery
                logger.info("Created new gallery: %s", gallery)

            cinema.save()
            logger.info("Saved cinema: %s", cinema)

            formset.instance = gallery
            formset.save()
            logger.info("Saved gallery images")

            messages.success(request, 'Кінотеатр успішно оновлено')
            return redirect('cinema_list')
        else:
            logger.warning("Form is invalid: %s, Formset is invalid: %s", form.errors, formset.errors)

    else:
        form = CinemaForm(instance=cinema)
        formset = GalleryImageFormSet(instance=gallery)
        logger.info("Loaded forms for GET request")

    return render(request, 'admin/edit_cinema.html', {'form': form, 'formset': formset,
                                                      'cinema': cinema, 'halls': halls})


# view for getting all cinemas
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
def cinema_list_view(request):
    cinemas = Cinema.objects.all()
    return render(request, 'admin/cinemas_list.html', {'cinemas': cinemas})


# view for get template for success cinema page
def cinema_success(request):
    return render(request, 'admin/cinema_success.html')


# view for delete cinema from DB
def delete_cinema(request, cinema_id):
    cinema = get_object_or_404(Cinema, id=cinema_id)

    if request.method == 'POST':
        cinema.delete()
        return redirect('cinema_list')

    return render(request, 'admin/delete_cinema_confirm.html', {'cinema': cinema})


# view for add new hall to the DB
@transaction.atomic
def add_hall(request, cinema_id):
    logger.info(f"cinema_id: {cinema_id}")
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
                        logger.error(f"Main image does not exist: {main_image_id.id}")
                        return render(request, 'admin/add_hall.html', {'form': form, 'formset': formset})

                # Save schema of hall
                schema_picture_id = form.cleaned_data['schema_picture']
                if schema_picture_id:
                    try:
                        schema_picture = GalleryImage.objects.get(pk=schema_picture_id.id)
                        hall.schema_picture = schema_picture
                    except GalleryImage.DoesNotExist:
                        messages.error(request, 'Картинка не існує.')
                        logger.error(f"Schema picture does not exist: {schema_picture_id.id}")
                        return render(request, 'admin/add_hall.html', {'form': form, 'formset': formset})

                # gallery
                gallery = Gallery.objects.create()
                hall.gallery = gallery
                hall.save()

                formset.instance = gallery
                formset.save()

                messages.success(request, 'Зал успішно додано.')
                return redirect('edit_cinema', cinema_id=cinema.id)  # Redirect to the cinema edit page
            except Exception as e:
                logger.error(f"An error occurred: {e}")
                messages.error(request, f"An error occurred: {e}")
        else:
            logger.error(f"Form is not valid: {form.errors}, {formset.errors}")

    else:
        form = HallForm()
        formset = GalleryImageFormSet()

    return render(request, 'admin/add_hall.html', {'form': form, 'formset': formset, 'cinema': cinema})


# view for edit hall model
@transaction.atomic
def edit_hall(request, hall_id):
    logger.info("Started editing cinema with ID %s", hall_id)
    hall = get_object_or_404(Hall, id=hall_id)
    cinema = hall.cinema_hall_id
    gallery = hall.gallery
    logger.info("Loaded hall: %s, gallery: %s,", hall, gallery)

    if request.method == "POST":
        logger.info("Processing POST request")
        form = HallForm(request.POST, request.FILES, instance=hall)
        formset = GalleryImageFormSet(request.POST, request.FILES, instance=gallery)

        if form.is_valid() and formset.is_valid():
            logger.info("Forms are valid")
            hall = form.save(commit=False)

            new_main_image_id = form.cleaned_data.get('main_image')
            if new_main_image_id:
                try:
                    new_main_image = GalleryImage.objects.get(pk=new_main_image_id.id)
                    if hall.main_image != new_main_image:
                        hall.main_image = new_main_image
                    logger.info("Updated main image: %s", new_main_image)
                except GalleryImage.DoesNotExist:
                    logger.error("Main image does not exist")
                    messages.error(request, 'Картинка не існує.')
                    return render(request, 'admin/add_cinema.html', {'form': form, 'formset': formset})
            else:
                hall.main_image = hall.main_image
                logger.info("Retained existing main image")

            new_schema_id = form.cleaned_data.get('schema_picture')
            if new_schema_id:
                try:
                    new_schema = GalleryImage.objects.get(pk=new_schema_id.id)
                    if hall.schema_picture != new_schema:
                        hall.schema_picture = new_schema
                    logger.info("Updated schema: %s", new_schema)
                except GalleryImage.DoesNotExist:
                    logger.error("Schema does not exist")
                    messages.error(request, 'Картинка не існує.')
                    return render(request, 'admin/add_cinema.html', {'form': form, 'formset': formset})
            else:
                hall.schema = hall.schema
                logger.info("Retained existing schema image")
            if not gallery:
                gallery = Gallery.objects.create()
                hall.gallery = gallery
                logger.info("Created new gallery: %s", gallery)

            hall.save()
            logger.info("Saved hall: %s", hall)

            formset.instance = gallery
            formset.save()
            logger.info("Saved gallery images")

            messages.success(request, 'Зал успішно оновлено')
            return redirect('edit_cinema', cinema_id=cinema)  # Redirect to the cinema edit page
        else:
            logger.warning("Form is invalid: %s, Formset is invalid: %s", form.errors, formset.errors)

    else:
        form = HallForm(instance=hall)
        formset = GalleryImageFormSet(instance=gallery)
        logger.info("Loaded forms for GET request")

    return render(request, 'admin/edit_hall.html', {'form': form,
                                                    'formset': formset, 'hall': hall})


# view for delete hall from the DB
def delete_hall(request, hall_id):
    hall = get_object_or_404(Hall, id=hall_id)
    cinema = hall.cinema_hall_id
    if request.method == 'POST':
        hall.delete()
        return redirect('edit_cinema', cinema_id=cinema)

    return render(request, 'admin/delete_hall_confirm.html', {'hall': hall, 'cinema': cinema})


# static view, will delete later
def our_cinemas(request):
    banner = [
        {
            'caption': 'Нема',
            'poster_url': ''}

    ]
    list_cinemas = [
        {
            'name': 'Супутник',
            'poster_url': '',
        },
        {
            'name': 'Мультиплекс',
            'poster_url': '',
        },
        {
            'name': 'Кіноман',
            'poster_url': '',
        },

    ]

    context = {'banner': banner, 'cinemas': list_cinemas}

    return render(request, 'cinemas/our_cinemas.html', context)


def cinema_detail(request):
    halls = Hall.objects.all()
    return render(request, 'admin/add_cinema.html', {'halls': halls})
