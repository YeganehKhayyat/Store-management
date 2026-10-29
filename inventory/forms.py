from django import forms
from inventory.models import FoodItem, Reservation

class FoodItemForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = [
            "title",
            "description",
            "category",
            "location",
            "quantity",
            "unit" , 
            "expired_date"
        ]
        
        
        