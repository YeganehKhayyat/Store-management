from datetime import timedelta

from django.utils import timezone

from inventory.models import FoodItem


def get_near_expiry_date():
    today = timezone.localdate()
    end_date = today + timedelta(days = 3)

    return FoodItem.objects.filter(
            expired_date__range= (
                today , end_date
            )
    )