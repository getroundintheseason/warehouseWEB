from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Collection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    artist = models.CharField(max_length=200, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    desciption = models.TextField(null=True, blank=True)
    bookcase = models.CharField(max_length=200, null=True, blank=True)

    isBorrow = models.BooleanField(default=False)
    borrowWho = models.CharField(max_length=200, null=True, blank=True, default='None')

    create = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['title']