from rest_framework import serializers
from .models import Album, Pic


class PicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pic
        fields = ['id','content','album']

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'title']