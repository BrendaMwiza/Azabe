
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Post(models.Model):
    name= models.CharField(max_length=60, null=True)
    description = models.CharField(max_length=60, null=True)
    location = models.CharField(max_length=60)
    time = models.CharField(max_length=60)
    user= models.ForeignKey(User,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.title)

    def save_post(self):
        self.save()

class Parents(models.Model):
    name = models.CharField(max_length=60)
    noChild = models.IntegerField()
    residence = models.CharField(max_length=60)
    email = models.CharField(max_length=60)

    def __str__(self):
        return str(self.name)

    def save_parent(self):
        self.save()


 
class Partners(models.Model):
    partner_name = models.CharField(max_length=60)
    description= models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    partner_image = models.ImageField(upload_to='partner/')

    def __str__(self):
        return str(self.partner_name)
        
    def save_partner(self):
        self.save()

class Activities(models.Model):
    partner_name = models.ForeignKey(Partners, on_delete=models.CASCADE, blank=True)
    activity_name = models.CharField(max_length=60)
    description= models.CharField(max_length=60)
    activity_image = models.ImageField(upload_to='activity/')
    price=models.CharField(max_length=60)
    
    def __str__(self):
        return str(self.activity_name)

    def save_activity(self):
        self.save()

class Child(models.Model):
    names=models.CharField(max_length=60)
    age = models.IntegerField()
    parent = models.ForeignKey(Parents,on_delete=models.CASCADE, blank=True)
    activity_id = models.ForeignKey(Activities, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.names)

    def save_child(self):
        self.save()
