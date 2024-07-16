from django.db import models
from django.utils import timezone
# Create your models here.


class Admin_model(models.Model):
    username= models.CharField(max_length=200)
    password= models.CharField(max_length=100)


    def __str__(self):
        return self.username


# adding food 
class Add_item(models.Model):
    item_name= models.CharField(max_length=2000)
    price=models.IntegerField()
    description=models.CharField(max_length=2000)
    available=models.BooleanField(default=True)

    def __str__(self):
        return self.item_name
    

class Today_item(models.Model):
    add_item = models.ForeignKey(Add_item, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.add_item.item_name} - {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
    
    
    @property
    def item_price(self):
        return self.add_item.price