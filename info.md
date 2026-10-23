# views tasks:

1- get requests

2- auth/perm

3- get input data

4- call service function

5- response redirect ...



# near expiry

expiry date < 3

expiry date <= 3    : boundry condition

expiry date 2025-10-18 00:00:00 utc | 2025-10-18 00:03:30 tehran

# sample in near expiry

today = timezone.localdate()

end_date = today + timedelta(days = 3)


FoodItem.objects.filter(
    expired_date__gt = today,
    expired_date__lte = end_date,
)

# challenge python :(

foods = FoodItem.objects.all()
for food in foods :
    print(food.is_near_expiry)


# Transaction atomic 
reservation = Reservation.objects.create(
        food_item = food_item,
        volunteer = volunteer,
        status = Reservation.Status.ACTIVE
)
    
food_item.status = FoodItem.Status.RESEREVED
food_item.save(
    update_fields = ['status']
)

SQL

insert (food_item , volunteer , status) values("milk" , "user1" , "active")

update set_status = 'reserved';

commit; / rollback;