from django.db import models
from django.db.models.deletion import SET_NULL



class Album(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title
    

class Pic(models.Model):
    content = models.TextField()
    album = models.ForeignKey(Album,on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "{}. {}".format(self.album, self.content)
    




