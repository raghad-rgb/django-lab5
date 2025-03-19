from django.db import models
from course_app.models import Track, Course
from django.utils.timezone import now

class Trainee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=1)
    creation_date = models.DateField(default=now)
    image = models.ImageField(upload_to='trainee/imgs/', null=True, blank=True)
    track = models.ForeignKey(Track, on_delete=models.CASCADE, null=True, blank=True) 
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
