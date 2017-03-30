from django.db import models


class Order(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()
    description = models.TextField()