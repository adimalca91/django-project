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


'''
This is model is used with a form inheriting the ModelForm class
The goal is to create a Form with ModelForm that the submitted data will be saved
in the Logger model / table / database.

So anyone who log-in their information will be save in this model!
'''    
class Logger(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    time_log = models.TimeField(help_text="Enter the exact time!")
    

'''
This is a model used with a form to accept user input on the booking page, connect with a database table
for storing the reservation requests received on the Little Lemon website.
Later the staff will be able to access and view this request from the Django administration control panel.
LAB-07: Working with Forms ->  Models > Models and Forms
'''
class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    guest_count = models.IntegerField()
    reservation_time = models.DateField(auto_now=True) # This default parameter set to True means it will not be displayed to the user in the webpage, only in the model / database table
    comments = models.CharField(max_length=200)