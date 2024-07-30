from django.contrib import admin
from django.urls import path
from src.core import views as pages_views
from src.cinemas import views as cinemas_views
from src.users import views as users_views
from src.movies import views as movies_views
from src.admin_pages import views as admin_pages_views
from src.promotion import views as promotion_views
from django.conf import settings
from django.conf.urls.static import static
from src.banners import views as banners_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('kino-cms/', pages_views.home_page),
    path('my-account/', users_views.client_page),
    path('contact-us/', pages_views.contact),

    # gallery admin
    path('upload_image/', pages_views.upload_image, name='upload_image'),
    path('get_gallery_images/', pages_views.get_gallery_images, name='get_gallery_images'),

    # movies admin
    path('movie/create/', movies_views.add_movie, name='add_movie'),
    path('movie_success/', movies_views.movie_success, name='movie_success'),
    path('movie/edit/<int:movie_id>/', movies_views.edit_movie, name='edit_movie'),
    path('movies/', movies_views.movie_list_view, name='movie_list'),
    path('movies/<int:movie_id>/delete/', movies_views.delete_movie, name='delete_movie'),

    # cinemas admin
    path('cinema/create/', cinemas_views.add_cinema, name='add_cinema'),
    path('cinema/edit/<int:cinema_id>/', cinemas_views.edit_cinema, name='edit_cinema'),
    path('cinema_success/', cinemas_views.cinema_success, name='cinema_success'),
    path('cinemas/', cinemas_views.cinema_list_view, name='cinema_list'),
    path('cinemas/<int:cinema_id>/delete/', cinemas_views.delete_cinema, name='delete_cinema'),

    # halls admin
    path('hall/create/<int:cinema_id>/', cinemas_views.add_hall, name='add_hall'),
    path('hall/edit/<int:hall_id>/', cinemas_views.edit_hall, name='edit_hall'),
    path('halls/<int:hall_id>/delete/', cinemas_views.delete_hall, name='delete_hall'),

    # pages admin
    path('page/create/', admin_pages_views.add_page, name='add_page'),
    path('page_success/', admin_pages_views.page_success, name='page_success'),
    path('page/edit/<int:page_id>/', admin_pages_views.edit_page, name='edit_page'),
    path('pages/all_pages/', admin_pages_views.page_list_view, name='all_page_list'),
    path('pages/<int:page_id>/delete/', admin_pages_views.delete_page, name='delete_page'),
    path('pages/main_page/', admin_pages_views.main_page, name='main_page'),
    path('pages/', admin_pages_views.pages_list, name='pages_list'),
    # path('pages/contacts', admin_pages_views.AddContactsView, name='add_contacts'),

    # posts admin
    path('post/create/', promotion_views.add_post, name='add_post'),
    path('post_success/', promotion_views.post_success, name='post_success'),
    path('post/edit/<int:post_id>/', promotion_views.edit_post, name='edit_post'),
    path('posts/', promotion_views.post_list_view, name='post_list'),
    path('posts/<int:post_id>/delete/', promotion_views.delete_post, name='delete_post'),

    # banners
    path('banners/main_page_banners', banners_views.main_banners, name='main_page_banner'),
    path('banners/main_page_news_banners', banners_views.news_banners, name='main_page_news_banner'),
    path('banners/back_banners', banners_views.back_banners, name='back_banner'),
    path('banners/banner-list/', banners_views.banner_list, name='banner_list'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


