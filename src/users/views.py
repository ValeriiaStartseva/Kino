from .models import User
from .forms import RegistrationForm, LoginForm, UserUpdateForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.db import transaction
from django.contrib import messages
from django.urls import reverse


def register(request):
    cities = ['Київ', 'Львів', 'Одеса', 'Харків', 'Дніпро']
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(form.cleaned_data.get('password1'))
            user.save()
            return JsonResponse({'form_is_valid': True, 'redirect_url': '/login/'})
        else:
            errors = {field: error[0] for field, error in form.errors.items()}
            return JsonResponse({'form_is_valid': False, 'errors': errors})
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form, 'cities': cities})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid email or password')
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('home')


def users_list_admin(request):
    if request.method == 'GET':
        users_list = User.objects.all().order_by('id')

        paginator = Paginator(users_list, 2)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        users_data = []
        for user in page_obj:
            page_data = {
                'id': user.id,
                'registration_date': user.date_joined,
                'date_birthday': user.date_birthday,
                'email': user.email,
                'phone': str(user.phone),
                'name': user.name,
                'last_name': user.last_name,
                'nickname': user.nickname,
                'city': user.city,
            }
            users_data.append(page_data)

        return render(request, 'admin/users_list.html', {'users': users_data, 'page_obj': page_obj})
    return JsonResponse({'error': 'Invalid request method'}, status=400)


@transaction.atomic
def edit_user(request, user_id):
    cities = ['Київ', 'Львів', 'Одеса', 'Харків', 'Дніпро']
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect(reverse('users_list'))
        else:
            messages.error(request, 'Form or data is not valid!!!')
    else:
        form = UserUpdateForm(instance=user)

    return render(request, 'admin/edit_user.html', {'form': form, 'user': user, 'cities': cities})


def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        user.delete()
        return redirect('users_list')

    return render(request, 'admin/confirm_delete_user.html', {'user': user})
