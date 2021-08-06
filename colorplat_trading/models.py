from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL

from django.contrib.auth.models import User


class ColorPlat(models.Model):
    name = models.CharField(max_length=150)
    owner = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    CreatedAt = models.DateTimeField(auto_now=True, null=True)

    # Colorplats have 3 color attributes
    rvalue = models.IntegerField(default=0)
    gvalue = models.IntegerField(default=0)
    bvalue = models.IntegerField(default=0)

    # Current 
    def currentprice(self):
        # Get latest price
        latestprice = ColorPrice.objects.all().order_by("-CreatedAt")[:1]
        return self.priceRGB(latestprice[0].priceRed,latestprice[0].priceGreen,latestprice[0].priceBlue)
    
    #RGB price model: price of a Colorplat depends on price of the individual components and their amount present in the attribute values
    def priceRGB(self,R,G,B):
        return (round(R*self.rvalue + G*self.gvalue + B*self.bvalue,2))


class ColorPrice(models.Model):
    priceRed = models.FloatField(default=0.0)
    priceGreen  = models.FloatField(default=0.0)
    priceBlue  = models.FloatField(default=0.0)
    CreatedAt = models.DateTimeField(auto_now=True, null=True)


class Trade(models.Model):
    fromaccount = models.ForeignKey(User,null=True,on_delete=models.SET_NULL,related_name='from_acc')
    toaccount = models.ForeignKey(User,null=True,on_delete=models.SET_NULL,related_name='to_acc')
    platsamount = models.IntegerField(default=0,null=False)
    amount = models.FloatField(default=0.0,null=False)
    CreatedAt = models.DateTimeField(auto_now=True, null=True)
    status = models.IntegerField(default=0,null=False)  #0: pending, 1: completed