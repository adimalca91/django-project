from django.db import models

# Create your models here.

'''
Here there are 2 models which are connected via one-to-many relationship because
many drinks can belong to one category.
'''

class DrinksCategory(models.Model):
    category_name = models.CharField(max_length=200)


'''
This is a model that will be used as a database for storing the different
menu items that are being displayed on the Little Lemon website.
'''
class Drinks(models.Model):
    # Django will create a default primary key called "id"
    drink = models.CharField(max_length=200)
    price = models.IntegerField()
    category_id = models.ForeignKey(DrinksCategory, on_delete=models.PROTECT, default=None)