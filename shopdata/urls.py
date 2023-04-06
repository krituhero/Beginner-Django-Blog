from django.contrib import admin
from django.urls import path
from shopdata import views
from django.conf.urls.static import static
from django.conf import settings
from .views import PostDetailView

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('submitcontact', views.submitcontact, name='submitcontact'),
    path('userpage', views.userpage, name='userpage'),
    path('loginuser', views.loginuser, name='loginuser'),
    path('signup', views.signup, name='signup'),
    path('logout', views.userlogout, name='logout'),
    path('blog', views.viewblog, name='viewblog'),
    path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)