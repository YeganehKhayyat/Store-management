from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
# Create your models here.

class FoodItem(models.Model):
    title = models.CharField(max_length=128)
    quantity = models.PositiveIntegerField()
    expired_date = models.DateTimeField()
    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=Q(quantity_gt = 0),
                name="fooditem_quantity_gt_zero"
            )
        ]
        
        indexes = models.Index(
            fields=['expired_date' , 'quantity'] , 
            name = "food_expired_idx"
        )
        
        
class Reservation(models.Model):
    class Status(models.TextChoices):
        ACTIVE = 'active' , 'Active'
        EXPIRED = 'expired' , 'Expired'
        
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    food_item = models.ForeignKey(FoodItem , on_delete=models.CASCADE)
    status = models.CharField(
        max_length=30 ,
        choices=Status.choices , 
        default = Status.ACTIVE
        )
    
    class Meta:
        constraints =  [
           models.UniqueConstraint(
               conditions = Q(status = 'active'),
               name = 'unique_active_reservation'
           )
        ]
    