from django.urls import path,re_path
from django.conf import settings
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('', views.welcome, name='welcome'),
    path('profile/<username>/', views.profile, name='profile'),
    path('addmoney_submission/',views.addmoney_submission,name='addmoney_submission'),
    path('edit_submission/<int:id>', views.edit_submission, name='edit_submission'),
    path('submission_detail/<int:id>',views.submission_detail, name='submission_detail'),
    path('submission_delete/<int:id>',views.submission_delete, name='submission_delete'),
    re_path(r'^search/', views.search_project,name='search_results'),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)