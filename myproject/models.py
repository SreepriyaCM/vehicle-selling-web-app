from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100,primary_key=True)
    category_img=models.ImageField(upload_to='categories')

    def __str__(self):
        return self.name

class Vehicles(models.Model):
    name=models.CharField(max_length=100)
    mileage=models.FloatField(null=True)
    distance_covered=models.IntegerField(null=True)
    description=models.TextField()
    fuel_type=models.CharField(max_length=100,null=True)
    color=models.CharField(max_length=50,null=True)
    manufacture_year=models.IntegerField(null=True)
    base_price=models.DecimalField(max_digits=10,decimal_places=2,null=True)
    image=models.ImageField(upload_to='vehicles')
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    best_selling=models.BooleanField(default=False,null=True)
    slug=models.SlugField()
    
    def __str__(self):
        return self.name


class Profiles(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    mob_no=models.IntegerField()
    address=models.TextField()
