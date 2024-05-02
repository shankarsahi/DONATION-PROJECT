

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Donor(models.Model):
    # user=models.ForeignKey(User,on_delete=models.CASCADE ,null=True)
    name = models.CharField( max_length=50,null=True)
    email=models.EmailField(null=True)
    contact = models.CharField( max_length=20,null=True)
    password=models.CharField( max_length=20,null=True)
    address = models.CharField( max_length=200,null=True) 
    donorpic = models.ImageField(upload_to="donorpic/", null=True)
    # regdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

   

  
class Volunteer(models.Model):
    # user=models.ForeignKey(User,on_delete=models.CASCADE ,null=True)
    name = models.CharField( max_length=50,null=True)
    email=models.EmailField(null=True)
    contact = models.CharField( max_length=20,null=True)
    password=models.CharField( max_length=20,null=True)
    address = models.CharField( max_length=200,null=True) 
    volunteerpic = models.FileField(upload_to="volunteer/",null=True)
    idpic = models.FileField(upload_to="volunteerid/",null=True)
    # adminremark = models.CharField( max_length=20,null=False)
    # regdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


class DonationArea(models.Model):
    areaname = models.CharField( max_length=50,null=True)
    description = models.CharField( max_length=100,null=True)
    creationdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.areaname


class Donation(models.Model):
    donor=models.ForeignKey(Donor,on_delete=models.CASCADE ,null=True)
    donorname = models.CharField( max_length=50,null=True)
    donationname = models.CharField( max_length=50,null=True)
    donationpic = models.FileField(upload_to="donationpic/",null=True) 
    collectionloc = models.CharField( max_length=50,null=True)
    description = models.CharField( max_length=50,null=True)
    status =  models.CharField( max_length=20,null=True)
    donationdate = models.DateTimeField(auto_now_add=True)
    adminremark = models.CharField( max_length=20,null=True)
    volunteerassign = models.CharField( max_length=20,null=True)
    donationarea = models.CharField( max_length=50,null=True)
    volunteerremark = models.CharField( max_length=20,null=True)
    updationdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.donorname