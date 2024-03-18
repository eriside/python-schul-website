"""
URL configuration for webinf12_gaertner project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from blog.views import home, betriebssysteme, bootstrap, impressum, lernplan, linksammlung, user_login, logout, dashboard, create_post, edit_post, delete_post,admin_dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('betriebssysteme/', betriebssysteme, name='betriebssysteme'),
    path('bootstrap/', bootstrap, name='Bootstrap'),
    path('impressum/', impressum, name='Impressum'),
    path('lernplan/', lernplan, name='lernplan'),
    path('linksammlung/', linksammlung, name='Linksammlung'),
    path('login/', user_login, name='Login'),
    path('logout/', logout, name='Logout'),
    path('aktuelles/', dashboard, name='Aktuelles'),
    path('create/', create_post, name='create_post'),
    path('dashboard/', admin_dashboard, name='admin_dashboard'),
    path('edit/<int:pk>/', edit_post, name='edit_post'),
    path('delete/<int:pk>/', delete_post, name='delete_post'), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

