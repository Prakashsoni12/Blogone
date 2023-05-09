import datetime
import os
from django.db import models
from django.db.models.deletion import SET_DEFAULT, SET_NULL
from django.contrib.auth.models import User

# Create your models here.


class BlogCategory(models.Model):
    name = models.CharField(max_length=190, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return self.name


def get_filename(instance, filename):
    old_name = filename
    current_time = datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    filename = "%s%s" % (current_time, old_name)
    return os.path.join('uploads/', filename)


class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(BlogCategory, on_delete=SET_NULL, null=True)
    title = models.CharField(max_length=150, null=True)
    image = models.ImageField(upload_to=get_filename, null=True,)
    description = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return self.title


class Myblog(models.Model):
    user = models.ForeignKey(User, on_delete=models.Case, null=False)
    blogss = models.ForeignKey(Blog, on_delete=models.Case, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
