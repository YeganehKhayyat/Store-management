#business Errors

class InventoryError(Exception):
    """
    Base Exception for excepted business error
    """
    
    
class FoodItemNotAvailableError(InventoryError):
    """
    
    """
    
class FoodItemExpired(InventoryError):
    """
    
    """
    

    