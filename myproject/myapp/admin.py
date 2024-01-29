from django.contrib import admin
from .models import Drinks, DrinksCategory, Logger, Booking, Employee, Menu

# Register your models here.

admin.site.register(Drinks)
admin.site.register(DrinksCategory)
admin.site.register(Logger)
admin.site.register(Booking)
admin.site.register(Employee)
admin.site.register(Menu)
