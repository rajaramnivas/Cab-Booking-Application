from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    ROLE_CHOICES=(
        
        ('CUSTOMER','Customer'),
        ('DRIVER','Driver'),
            
    )
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    role=models.CharField(max_length=200,choices=ROLE_CHOICES)

class Ride(models.Model):
    STATUS_CHOICE=(
        ('REQUESTED','Requested'),
        ('ACCEPTED','Accepted'),
        ('STARTED','Started'),
        ('COMPLETED','Completed'),
        ('CANCELD','Canceled'),
    )
    
    customer=models.ForeignKey(User,on_delete=models.CASCADE,related_name='customer_ride')
    driver=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name='driver_ride')
    pickup_location=models.CharField(max_length=200)
    drop_location=models.CharField(max_length=200)    
    fare=models.IntegerField()
    status=models.CharField(max_length=200,choices=STATUS_CHOICE,default='REQUESTED')
    created_at=models.DateTimeField(auto_now_add=True)
    