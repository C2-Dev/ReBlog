from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.tab2, name='tab2'),
    path('accounts/profile/', RedirectView.as_view(url='/'), name = 'profile'),
    url('login', auth_views.LoginView.as_view(), name='login'),
    url('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('post', views.tab1, name = 'tab1'),
    path('profile', views.tab3, name = 'tab3'),
]