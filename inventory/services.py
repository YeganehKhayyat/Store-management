from django.core.exceptions import ValidationError
from django.utils import timezone

from inventory.models import FoodItem, Reservation

def reserve_food_item(* , food_item , volunteer):
    if food_item.status != FoodItem.Status.AVAILABLE:
        raise ValidationError(
            "This food item is not available."
        )
    
    if food_item.expired_date < timezone.localdate():
        raise ValidationError(
            "Expired food cannot be reserved."
        )
        
    if Reservation.objects.filter(
        food_item = food_item,
        status = Reservation.Status.ACTIVE
    ).exists():
        raise ValidationError(
            "This food item already has an active reservation."
        )
        
    reservation = Reservation.objects.create(
        food_item = food_item,
        volunteer = volunteer,
        status = Reservation.Status.ACTIVE
    )
    
    food_item.status = FoodItem.Status.RESEREVED
    food_item.save(
        update_fields = ['status']
    )
    return reservation