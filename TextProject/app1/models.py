from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Tag(models.Model):
    title=models.CharField(max_length=250,unique=True)

    def __str__(self):
        return self.title

class Snippet(models.Model):
    title=models.CharField(max_length=200)
    content=models.CharField(max_length=250)
    createdby=models.ForeignKey(User,on_delete=models.CASCADE)
    tag=models.ForeignKey(Tag,on_delete=models.CASCADE,related_name="snippet")
    timestamp=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title


