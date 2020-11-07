from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as erp_views

urlpatterns = [
    path('', erp_views.home, name='erp-home'),
    path('login/', auth_views.LoginView.as_view(template_name='erp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='erp/logout.html'), name='logout'),
]