from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .models import Album, Pic
from .serializers import PicSerializer, AlbumSerializer

# SUAS OUTRAS FUNÇÕES CONTINUAM AQUI


def index (request):
    return render("Oi")

@api_view(['GET', 'POST'])
def api_pic_get(request, pic_id):
    try:
        pic = Pic.objects.get(id=pic_id)
    except Pic.DoesNotExist:
        raise Http404()

    
    serialized_pic = PicSerializer(pic)
    return Response(serialized_pic.data)

@api_view(['GET', 'POST'])

def api_pic_post(request):
    if request.method == 'POST':
        new_pic_data = request.data
        pic = Pic()
        pic.content = new_pic_data['content']

        if Album.objects.filter(title = new_pic_data['album']).exists():
            album = Album.objects.get(title=new_pic_data['album'])
            pic.album = album
            pic.save()

        else:
            album = Album()
            album.title = new_pic_data['album']
            album.save()
            pic.album = album
            pic.save()

       

    
    serialized_pic = PicSerializer(pic)
    return Response(serialized_pic.data)

@api_view(['GET', 'POST'])

def api_album_get(request,album_id):
    
    album = Album.objects.get(title=album_id)

    pics = Pic.objects.filter(album=album.id)
    serialized_pics = PicSerializer(pics,many=True)
    return Response(serialized_pics.data)

@api_view(['GET', 'POST'])
def api_albums_get(request):
    
    albums = Album.objects.all()
    serialized_albums = AlbumSerializer(albums, many=True)
    return Response(serialized_albums.data)
    

@api_view(['GET', 'POST'])

def api_album_post(request):
    if request.method == 'POST':
        new_album_data = request.data
        album = Album()
        album.title = new_album_data['title']
        album.save()
    
    serialized_album = AlbumSerializer(album)
    return Response(serialized_album.data)

