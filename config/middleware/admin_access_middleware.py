from django.shortcuts import redirect
from django.urls import reverse


class AdminAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # check if user on login admin page
        login_url = reverse('custom_admin_login')

        if request.path.startswith('/admin/') and not request.user.is_superuser:
            if request.path != login_url:
                return redirect(login_url)

        response = self.get_response(request)
        return response
