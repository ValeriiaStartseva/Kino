from django.shortcuts import render


def client_page(request):
    return render(request, 'users/user_acc.html')





