from django.db import models
from customers.models import Customers
from products.models import Product
class Order(models.Model):
    
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((LIVE,'Live'),(DELETE,'Delete'))
    #here we add the stages of the order
    CART_STAGE =0
    ORDER_CONFIRMED = 1
    ORDER_PROCESSED = 2
    ORDER_DELIVERED = 3
    ORDER_REJECTED = 4
    #ASSIGN THE VALUES IN TUPLES

    STATUS_CHOICES = ((ORDER_PROCESSED,"ORDER_PROCESSED"),
                      (ORDER_DELIVERED,"ORDER_DELIVERED"),
                      (ORDER_REJECTED,"ORDER_REJECTED"))   # her only three choices are given as only these three can be changed from the admin end
    
    order_status= models.IntegerField(choices=STATUS_CHOICES, default=CART_STAGE)#her default is given as cart stage as, if a user order something for the first time it should be in a cart with no other products

    owner = models.ForeignKey(Customers, on_delete=models.SET_NULL , null=True, related_name='Customer_profil')   #ororo cart num oru admin undaavum
    delete_status = models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at =models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now=True)

class orderedItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,related_name='added_carts',null=True) 
    quantity = models.IntegerField(default=1)
    owner = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='added_items')
