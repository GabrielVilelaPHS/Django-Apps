from django.urls import path

from . import views

urlpatterns = [

    #tanto home quanto page são funções criadas nas views

    path('', views.home, name = 'home' )
    path('index.html/', views.page, name = 'index')
    
]