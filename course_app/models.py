from django.db import models

class Track(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    track = models.ForeignKey(Track, on_delete=models.CASCADE, default=1) 

    def __str__(self):
        return self.title
