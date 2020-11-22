from django.db import models

class products(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=200)
    processmaking = models.CharField(max_length=200)


