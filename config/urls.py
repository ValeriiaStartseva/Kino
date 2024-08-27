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
from src.newsletter import views as newsletter_views

urlpatterns = [


    path('admin/', admin.site.urls),
    path('kino-cms/', pages_views.home_page),



    # home page
    path('', pages_views.home_page, name="home"),

    # pages site
    path('movies/<slug:slug>/', pages_views.movie_detail, name='movie_detail'),
    path('cinemas/<slug:slug>/', pages_views.cinema_detail, name='cinema_detail'),
    path('halls/<slug:slug>/', pages_views.hall_detail, name='hall_detail'),
    path('billboard/', pages_views.billboard, name='billboard'),
    path('coming-soon/', pages_views.coming_soon, name='coming_soon'),
    path('pages/<slug:slug>/', pages_views.page_detail, name='page_detail'),
    path('promotions/', pages_views.promotions, name='promotions'),
    path('promotion/<slug:slug>/', pages_views.promotion_detail, name='promotion_detail'),
    path('news/', pages_views.news, name='news'),
    path('news/<slug:slug>/', pages_views.news_detail, name='news_detail'),
    path('contact-us/', pages_views.contact, name='contact_us'),
    path('timetable/', pages_views.timetable_view, name='timetable'),
    path('booking/<int:showtime_id>/', pages_views.booking_view, name='booking'),




    # user site
    path('register/', users_views.register, name='register'),
    path('login/', users_views.login, name='login'),
    path('logout', users_views.logout, name='logout'),

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
    path('pages/contacts', admin_pages_views.contacts_view, name='add_contacts'),

    # posts admin
    path('post/create/', promotion_views.add_post, name='add_post'),
    path('post_success/', promotion_views.post_success, name='post_success'),
    path('post/edit/<int:post_id>/', promotion_views.edit_post, name='edit_post'),
    path('posts/', promotion_views.post_list_view, name='post_list'),
    path('posts/<int:post_id>/delete/', promotion_views.delete_post, name='delete_post'),

    # banners admin
    path('banners/main_page_banners', banners_views.main_banners, name='main_page_banner'),
    path('banners/main_page_news_banners', banners_views.news_banners, name='main_page_news_banner'),
    path('banners/back_banners', banners_views.back_banners, name='back_banner'),
    path('banners/banner-list/', banners_views.banner_list, name='banner_list'),


    # users admin
    path('users/', users_views.users_list_admin, name='users_list'),
    path('users/<int:user_id>/delete/', users_views.delete_user, name='delete_user'),
    path('user/edit/<int:user_id>/', users_views.edit_user, name='edit_user'),


    # email newsletter
    path('email-campaign/', newsletter_views.email_campaign_view, name='email_campaign'),
    path('save-selected-users/', newsletter_views.save_selected_users, name='save_selected_users'),
    path('delete-template/<int:template_id>/', newsletter_views.delete_template, name='delete_template'),
    path('email-campaign/progress/<int:campaign_id>/', newsletter_views.check_campaign_progress, name='check_campaign_progress'),

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


