from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/pics/<int:pic_id>/', views.api_pic_get),
    path('api/pics/',views.api_pic_post),
    path('api/album/<str:album_id>/', views.api_album_get),
    path('api/album/',views.api_album_post),
    path('api/albums/', views.api_albums_get)

]