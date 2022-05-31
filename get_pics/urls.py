from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='gallery'),
    path('picture/<str:pk>/',views.viewPicture,name='album'),
    
    path('search/',views.searchPicture,name='search')
    
    ]