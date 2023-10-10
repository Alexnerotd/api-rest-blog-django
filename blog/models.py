from django.db import models
from authentication.models import MyUser

# Create your models here.


class Blog(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    title = models.CharField("Title", max_length=50, unique=True)
    description = models.CharField("Description", max_length=50, unique=True)
    content = models.TextField()


    def __str__(self):
        return f"{self.title}"
    