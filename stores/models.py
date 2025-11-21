from django.db import models

# Create your models here.
class category(models.Model):
    title=models.CharField(max_length=225)
    image=models.ImageField(upload_to='category', null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=False)

    #collection
class collection(models.Model):
    title=models.CharField(max_length=225)
