from django.db import models

# Create your models here.


class Items(models.Model):
    Name=models.CharField(max_length=200)
    price=models.FloatField(blank=True)
    picture=models.ImageField(null=True)

class shipping_info(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    zipcode=models.CharField(max_length=20)
    citystate=models.CharField(max_length=100)




class user(models.Model):
    ipaddress=models.GenericIPAddressField()
    item = models.ManyToManyField(Items, null=True, blank=True)
    quanity1 = models.IntegerField(default=1)
    quanity2 = models.IntegerField(default=1)
    quanity3 = models.IntegerField(default=1)
    quanity4 = models.IntegerField(default=1)
    shipping=models.ForeignKey(shipping_info, on_delete=models.CASCADE, null=True, blank=True)


