from django.contrib import admin
from inventory.models import FoodItem, Reservation, Category,FoodLocation
# Register your models here.
admin.site.register(FoodItem)
admin.site.register(Reservation)
admin.site.register(Category)
admin.site.register(FoodLocation)