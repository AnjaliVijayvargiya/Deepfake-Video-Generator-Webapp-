from django.db import models

# Create your models here.
class video(models.Model):
    video1 = models.FileField(upload_to="videos1/",null=True)
    video2 = models.FileField(upload_to="videos2/",null=True)

class video2(models.Model):
    image = models.ImageField(upload_to="image/",null=True)
    video3 = models.FileField(upload_to="videos3/",null=True)
