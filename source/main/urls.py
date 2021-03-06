"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from webapp.views import index_view, book_create_view, guest_update_view, guest_delete_view, search_guest

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('book/add/', book_create_view, name='book_create'),
    path('guest/<int:pk>/edit/', guest_update_view, name='update_view'),
    path('guest/<int:pk>/delete', guest_delete_view, name='delete_view'),
    path('guest/search/', search_guest, name='search_guest')

]
