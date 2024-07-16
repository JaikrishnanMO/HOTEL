from django.db import models
from base.models import Today_item,Add_item

# class Order_food(models.Model):
#     TABLE_CHOICES = [
#         ('A1', 'A1'),
#         ('A2', 'A2'),
#         ('B1', 'B1'),
#         ('B2', 'B2'),
#         ('C1', 'C1'),
#         ('C2', 'C2'),
#         ('D1', 'D1'),
#         ('D2', 'D2'),
#     ]
#     item_name = models.ManyToManyField(Today_item)
#     quantity = models.IntegerField()
#     table = models.CharField(max_length=3, choices=TABLE_CHOICES)
#     approve = models.BooleanField(default=False)
    
#     def __str__(self):
#         items_str = ', '.join(str(item.add_item.item_name) for item in self.item_name.all())
#         return f"{items_str} - Table: {self.table} - Quantity: {self.quantity}"

TABLE_CHOICES = [
    ('A1', 'A1'),
    ('A2', 'A2'),
    ('B1', 'B1'),
    ('B2', 'B2'),
    ('C1', 'C1'),
    ('C2', 'C2'),
    ('D1', 'D1'),
    ('D2', 'D2'),
]

class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    table = models.CharField(max_length=2, choices=TABLE_CHOICES)
    approve = models.BooleanField(default=False)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Add_item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_price(self):
        return self.item.price * self.quantity