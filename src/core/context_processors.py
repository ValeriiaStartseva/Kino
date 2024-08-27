from src.admin_pages.models import Page


def navbar_pages(request):
    pages = Page.objects.filter(status=True)
    return {'pages': pages}


def footer_pages(request):
    pages = Page.objects.filter(status=True)
    return {'pages': pages}
