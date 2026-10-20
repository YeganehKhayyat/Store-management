from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class FoodItem(models.Model):
    class Status(models.TextChoices):
        AVAILABLE = 'available' , 'Available'
        RESEREVED = 'reserved' , 'Reserved'
        EXPIRED = 'expired' , 'Expired'
        
    title = models.CharField(max_length=128)
    quantity = models.PositiveIntegerField()
    expired_date = models.DateField()
    
    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=Q(quantity__gt = 0),
                name="fooditem_quantity_gt_zero"
            )
        ]
        
        indexes = [models.Index(
            fields=['expired_date' , 'quantity'] , 
            name = "food_expired_idx"
        )
        ]
        
    @property    
    def days_until_expiry(self):
        return (
            self.expired_date - timezone.localdate()
        ).days
        
    @property
    def is_expired(self):
        return self.expired_date < timezone.localdate()    

    @property
    def near_expiry(self):
        days = self.days_until_expiry
        
        return 0 <= days <= 3
    
    def __str__(self):
        return f"{self.title} -- {self.expired_date} -- {self.quantity}"
        
        
class Reservation(models.Model):
    class Status(models.TextChoices):
        ACTIVE = 'active' , 'Active'
        CANCEL = 'cancel' , 'Cancel'
        COMPLETED = 'completed' , 'Completed'
        
    volunteer = models.ForeignKey(User , on_delete=models.CASCADE)
    food_item = models.ForeignKey(FoodItem , on_delete=models.CASCADE)
    status = models.CharField(
        max_length=30 ,
        choices=Status.choices , 
        default = Status.ACTIVE
        )
    
    class Meta:
        constraints =  [
           models.UniqueConstraint(
               fields = ['volunteer' , 'food_item'],
               condition = Q(status = 'active'),
               name = 'unique_active_reservation'
           )
        ]
    