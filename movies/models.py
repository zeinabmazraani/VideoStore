from django.db import models

class Video(models.Model):
    MovieID = models.AutoField(primary_key=True)
    MovieTitle = models.CharField(max_length=200)
    Actor1Name = models.CharField(max_length=100, null=True, blank=True)
    Actor2Name = models.CharField(max_length=100, blank=True, null=True)   
    DirectorName = models.CharField(max_length=100, null=True, blank=True)
    MovieGenre = models.CharField(max_length=50, null=True, blank=True)
    ReleaseYear = models.PositiveIntegerField(null=True, blank=True)
    Description = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.MovieTitle
