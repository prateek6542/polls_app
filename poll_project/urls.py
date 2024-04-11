from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from poll import views as poll_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', poll_views.home, name='home'),
    path('create/', poll_views.create, name='create'),
    path('vote/<poll_id>/', poll_views.vote, name='vote'),
    path('results/<poll_id>/', poll_views.results, name='results'),
    path('', poll_views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='poll/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='poll/logout.html'), name='logout'),
]