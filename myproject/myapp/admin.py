from django.contrib import admin
from .models import Drinks, DrinksCategory, Logger, Booking

# Register your models here.

admin.site.register(Drinks)
admin.site.register(DrinksCategory)
admin.site.register(Logger)
admin.site.register(Booking)
