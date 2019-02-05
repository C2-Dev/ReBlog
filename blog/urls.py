from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/profile/', RedirectView.as_view(url='/'), name = 'profile'),
    path('update_profile', views.update_profile, name = 'update_profile'),
    url('login', auth_views.LoginView.as_view(), name='login'),
    url('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('post', views.post_new, name = 'post_new'),
]