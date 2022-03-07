from django.urls import path,re_path
from django.conf import settings
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('', views.welcome, name='welcome'),
    path('profile/<username>/', views.profile, name='profile'),
    path('addmoney_submission/',views.addmoney_submission,name='addmoney_submission'),
    re_path(r'^search/', views.search_project,name='search_results'),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)