from django.db import models

# Create your models here.

'''
This is a model that will be used as a database for storing the different
menu items that are being displayed on the Little Lemon website.
'''
class Drinks(models.Model):
    # Django will create a default primary key called "id"
    drink_name = models.CharField(max_length=200)
    price = models.IntegerField()