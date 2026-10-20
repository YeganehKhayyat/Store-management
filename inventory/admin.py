from django.contrib import admin
from inventory.models import FoodItem, Reservation
# Register your models here.
admin.site.register(FoodItem)
admin.site.register(Reservation)