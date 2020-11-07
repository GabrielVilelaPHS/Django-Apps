"""breakOFdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static #poque vamos estar adiciconando ao estatico como MIDIA

from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('BlogApp.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')) 
    '''
    O paocte ckeditor se comporta como o app, 
    por isso tem que colocar no urls o que na verdade seria u diretório.
    '''
]+static(settings.MEDIA_URL)
