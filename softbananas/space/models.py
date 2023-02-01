from django.db import models


# Create your models here.

class Category(models.Model):
    category = models.TextField(max_length=30)
