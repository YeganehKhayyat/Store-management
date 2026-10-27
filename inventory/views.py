from django.shortcuts import (
    redirect,
    get_object_or_404,
    render
    ) 
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required , permission_required
from django.contrib import messages
from django.http import HttpResponseNotAllowed
from django.core.exceptions import ValidationError

from inventory.services import reserve_food_item , donate_reserve_food
from inventory.models import FoodItem , Reservation
from inventory.reports import get_category_report
# Create your views here.

# @login_required
# def reserve_food(request , pk):
    
#     item = get_object_or_404(
#         FoodItem , 
#         pk = pk
#     )
    
#     if request.method != "POST":
#         return redirect(
#             "food_detail" , 
#             pk = item.pk
#         )
    
#     try:              # For raise ValidationError in services
#         reserve_food_item(
#             food_item_id= pk ,
#             volunteer= request.user
#         )
#     except ValidationError as exc:
#         messages.error(
#             request , 
#             exc.messages
#         ) 
#     else:
#          messages.success(
#              request ,
#              "رزرو با موفقیت انجام شد."
#          )  
    
#     return redirect (
#         "food_detail" , 
#         pk = item.pk
#     )  
    
# @login_required
# def donate_food(request , pk):
#     if request.method != "POST":
#         return HttpResponseNotAllowed(["GET"])
    
#     try:
#         donate_reserve_food(
#             reservation_id=pk
#             )
        
#     except ValidationError as exc:
#         messages.error(
#             request ,
#             exc.messages
#             )
        
#     else:
#         messages.success(
#             request , 
#             "تحویل با موفقیت انجام شد."
#         )
        
#     return redirect("reservation_list")

@login_required
@permission_required(
    "inventory.view_food_reports",
    raise_exception=True
)
def dashboard(request):
    category_report = get_category_report()
    return render(
        request ,
        "dashboard.html",
        {'category_report' : category_report}
    )
    