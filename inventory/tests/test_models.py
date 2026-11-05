from datetime import date , timedelta
from unittest.mock import patch

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db import transaction , IntegrityError

from inventory.models import (
    FoodItem ,
    Reservation ,
    Category ,
    FoodLocation
    )

User = get_user_model()

class FoodItemTestCase(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="test_manager" , 
            password= "test-password-123"
        )
        
        cls.category = Category.objects.create(
            title = "Dairy"
        )
        
        cls.location = FoodLocation.objects.create(
            title = "Main Fridge"
        )
        
    def create_food(self , expired_date):
        return FoodItem.objects.create(
            title = "Milk" , 
            category = self.category,
            location = self.location,
            quantity = 5 ,
            unit = FoodItem.Units.PIECE,
            expired_date = expired_date,
            created_by = self.user,
        )
        
    @patch(
        "inventory.models.timezone.localdate",
        return_value = date(2026 , 11 , 20)
    )
    
    def test_expired_food(self , mock_date):
        food = self.create_food(
            expired_date = date(2026, 11, 19)
        )
        result = food.is_expired
        self.assertTrue(result)
    
    @patch(
        "inventory.models.timezone.localdate",
        return_value = date(2026 , 11 , 20)
    )
    
    def test_food_expiring_today(self, mock_date):
        
        food = self.create_food(
            expired_date=date(2026 , 11 , 20)
        )  
        
        self.assertFalse(food.is_expired)
        self.assertTrue(food.near_expiry)
        
    @patch(
        "inventory.models.timezone.localdate",
        return_value = date(2026 , 11 , 20)
        )
        
    def test_near_expiry_boundry(self, mock_date):
            
        food = self.create_food(
                expired_date=date(2026 , 11 , 23)
            )  
            
        self.assertFalse(food.near_expiry)
        self.assertEqual(food.days_until_expiry, 3)
        
    def quantity_cannot_be_zero(self):
        
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                self.create_food(
                    expired_date=date(2026, 10 , 25)
                )
                FoodItem.objects.filter(
                    title = "Milk"
                ).update(quantity = 0)