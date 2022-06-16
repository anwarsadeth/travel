from django.db import models

# Create your models here.
class place(models.Model):
    objects = None
    name=models.CharField(max_length=200)
    img=models.ImageField(upload_to='imgs')
    details=models.TextField()
class destination(models.Model):
    objects = None
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='imgs')
    details=models.TextField()

    def __str__(self):
       return self.name