from django.shortcuts import render

# Create your views here.
def clean_quantity(self):
    quantity = self.cleaned_data['quantity']
    
    if quantity <= 0 :
        raise form.ValidationError(
            "quantity must bigger than zero"
        )
        
    return quantity

# url -> view -> form -> db

# django shell -> python manage.py shell
# FoodItem.objects.create()

# FoodItem.objects.filter(expired_date = "2026-10-15 00:00:00", quantitty_gt = 0)