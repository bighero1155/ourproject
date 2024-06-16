from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Gender(models.Model):
    gender_id = models.BigAutoField(primary_key=True, blank=False)
    gender = models.CharField(max_length=55, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'genders'

    def __str__(self):
        return self.gender    

class Customer(models.Model):
    customer_id = models.BigAutoField(primary_key=True, blank=False)
    first_name = models.CharField(max_length=55, blank=False)
    middle_name = models.CharField(max_length=55, blank=True)  
    last_name = models.CharField(max_length=55, blank=False)   
    email = models.EmailField()
    contact = models.CharField(max_length=12)   
    age = models.IntegerField(blank=False)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True) 
    date_updated = models.DateTimeField(auto_now=True)
    birth_date = models.DateField(blank=False)

    class Meta:
        db_table = 'customers'

class tbl_Authentication(models.Model):
    Empcode = models.IntegerField()
    username = models.CharField(max_length=50,default='')
    password = models.CharField(max_length=50,default='')
    is_active = models.IntegerField(null=True)
 
    def __str__(self):
        return self.username
 
    empAuth_objects = models.Manager()
