from django.db import models
from django.utils import timezone

# Create your models here.

class Company(models.Model):
    name     = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    phone    = models.IntegerField()

    def __str__(self):
      return self.name

class Employee(models.Model):
   company    = models.ForeignKey(Company, on_delete=models.CASCADE)
   name       = models.CharField(max_length=120)
   phone      = models.IntegerField()
   department = models.CharField(max_length=120)

   def __str__(self):
       return self.name
   

class Asset(models.Model):
    name           = models.CharField(max_length=120)
    model          = models.CharField(max_length=100)
    brand          = models.CharField(max_length=100)
    purchased_date = models.DateTimeField(default=timezone.now)
    condition      = models.TextField()
    issued         = models.BooleanField(default=False)

    def __str__(self):
       return self.name + " "+ self.brand
    
class AssetLog(models.Model):
   asset = models.ForeignKey(Asset, on_delete=models.CASCADE, null=True, blank=True)
   employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
   checkout_date = models.DateTimeField()
   return_date = models.DateTimeField(null=True, blank=True)
   checkout_condition = models.TextField()
   return_condition = models.TextField(null=True, blank=True)


