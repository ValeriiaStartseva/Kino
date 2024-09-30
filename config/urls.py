from django.urls import path, include
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
from django.conf.urls.i18n import i18n_patterns


admin_urlpatterns = [
    # user admin
    path('admin/login/', users_views.custom_admin_login, name='custom_admin_login'),
    path('admin/logout/', users_views.custom_admin_logout, name='custom_admin_logout'),


    # gallery admin
    path('admin/upload_image/', pages_views.upload_image, name='upload_image'),
    path('get_gallery_images/', pages_views.get_gallery_images, name='get_gallery_images'),  # url for get img from DB
    path('media/<path:path>/',  pages_views.serve_media, name='serve_media'),
    # movies admin
    path('admin/movie/create/', movies_views.add_movie, name='add_movie'),
    # path('admin/movie_success/', movies_views.movie_success, name='movie_success'),
    path('admin/movie/edit/<int:movie_id>/', movies_views.edit_movie, name='edit_movie'),
    path('admin/movies/', movies_views.movie_list_view, name='movie_list'),
    path('admin/movies/<int:movie_id>/delete/', movies_views.delete_movie, name='delete_movie'),

    # cinemas admin
    path('admin/cinema/create/', cinemas_views.add_cinema, name='add_cinema'),
    path('admin/cinema/edit/<int:cinema_id>/', cinemas_views.edit_cinema, name='edit_cinema'),
    path('admin/cinema_success/', cinemas_views.cinema_success, name='cinema_success'),
    path('admin/cinemas_admin/', cinemas_views.cinema_list_view, name='cinema_list'),
    path('admin/cinemas/<int:cinema_id>/delete/', cinemas_views.delete_cinema, name='delete_cinema'),

    # halls admin
    path('admin/hall/create/<int:cinema_id>/', cinemas_views.add_hall, name='add_hall'),
    path('admin/hall/edit/<int:hall_id>/', cinemas_views.edit_hall, name='edit_hall'),
    path('admin/halls/<int:hall_id>/delete/', cinemas_views.delete_hall, name='delete_hall'),

    # pages admin
    path('admin/page/create/', admin_pages_views.add_page, name='add_page'),
    path('admin/page_success/', admin_pages_views.page_success, name='page_success'),
    path('admin/page/edit/<int:page_id>/', admin_pages_views.edit_page, name='edit_page'),
    path('admin/pages/all_pages/', admin_pages_views.page_list_view, name='all_page_list'),
    path('admin/pages/<int:page_id>/delete/', admin_pages_views.delete_page, name='delete_page'),
    path('admin/pages/main_page/', admin_pages_views.main_page, name='main_page'),
    path('admin/pages/', admin_pages_views.pages_list, name='pages_list'),
    path('admin/pages/contacts', admin_pages_views.contacts_view, name='add_contacts'),

    # posts admin
    path('admin/post/create/', promotion_views.add_post, name='add_post'),
    path('admin/post_success/', promotion_views.post_success, name='post_success'),
    path('admin/post/edit/<int:post_id>/', promotion_views.edit_post, name='edit_post'),
    path('admin/posts/', promotion_views.post_list_view, name='post_list'),
    path('admin/posts/<int:post_id>/delete/', promotion_views.delete_post, name='delete_post'),

    # banners admin
    path('admin/banners/main_page_banners', banners_views.main_banners, name='main_page_banner'),
    path('admin/banners/main_page_news_banners', banners_views.news_banners, name='main_page_news_banner'),
    path('admin/banners/back_banners', banners_views.back_banners, name='back_banner'),
    path('admin/banners/banner-list/', banners_views.banner_list, name='banner_list'),


    # users - clients admin
    path('admin/users/', users_views.users_list_admin, name='users_list'),
    path('admin/users/<int:user_id>/delete/', users_views.delete_user, name='delete_user'),
    path('admin/user/edit/<int:user_id>/', users_views.edit_user, name='edit_user'),


    # email newsletter
    path('admin/email-campaign/', newsletter_views.email_campaign_view, name='email_campaign'),
    path('admin/save-selected-users/', newsletter_views.save_selected_users, name='save_selected_users'),
    path('admin/delete-template/<int:template_id>/', newsletter_views.delete_template, name='delete_template'),
    path('admin/email-campaign/progress/<int:campaign_id>/', newsletter_views.check_campaign_progress,
         name='check_campaign_progress'),
]
urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('admin/login/', users_views.custom_admin_login, name='custom_admin_login'),
    path('admin/dashboard/', admin_pages_views.admin_dashboard, name='admin_dashboard'),
    path('kino-cms/', pages_views.home_page, name='home'),

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
    path('contact-us/', pages_views.contact_view, name='contact_us'),
    path('timetable/', pages_views.timetable_view, name='timetable'),
    path('booking/<int:showtime_id>/', pages_views.booking_view, name='booking'),
    path('cinemas/', pages_views.cinemas_view, name='cinemas'),
    path('search/', pages_views.search_view, name='search'),



    # user site
    path('register/', users_views.register, name='register'),
    path('login/', users_views.login, name='login'),
    path('logout', users_views.logout, name='logout'),



) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += admin_urlpatterns
