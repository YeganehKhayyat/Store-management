from django.shortcuts import (
    redirect,
    get_object_or_404  
    ) 
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.core.exceptions import ValidationError

from inventory.services import reserve_food_item
from inventory.models import FoodItem , Reservation
# Create your views here.

@login_required
def reserve_food(request , pk):
    
    item = get_object_or_404(
        FoodItem , 
        pk = pk
    )
    
    if request.method != "POST":
        return redirect(
            "food_detail" , 
            pk = item.pk
        )
    
    try:                                # For raise ValidationError in services
        reserve_food_item(
            food_item= item ,
            volunteer= request.user
        )
    except ValidationError as exc:
        messages.error(
            request , 
            exc.messages
        ) 
    else:
         messages.success(
             request ,
             "رزرو با موفقیت انجام شد."
         )  
    
    return redirect (
        "food_detail" , 
        pk = item.pk
    )  