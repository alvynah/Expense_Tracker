from django.urls import path,re_path
from django.conf import settings
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
     path('profile/<username>/', views.profile, name='profile'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)