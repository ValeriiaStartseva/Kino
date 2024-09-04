from src.admin_pages.models import Page
from src.banners.models import BackgroundBanner


# this is func for right displaying navbar abd footer for all site
def navbar_pages(request):
    pages = Page.objects.filter(status=True)
    return {'pages': pages}


def footer_pages(request):
    pages = Page.objects.filter(status=True)
    return {'pages': pages}


def background_banner_processor(request):
    background_banner = BackgroundBanner.objects.last()
    return {'background_banner': background_banner}
