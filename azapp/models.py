
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.utils.timezone import utc
from datetime import datetime

# Create your models here.
class Post(models.Model):
    name= models.CharField(max_length=60, null=True)
    description = models.CharField(max_length=60, null=True)
    location = models.CharField(max_length=60,null=True)
    time = models.DateTimeField(auto_now=True, null=True)
    user= models.ForeignKey(User,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.name)

    def save_post(self):
        self.save()

class Parents(models.Model):
    name = models.CharField(max_length=60,null=True)
    noChild = models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE, blank=True,null=True)
    location = models.CharField(max_length=60,null=True)
    email = models.CharField(max_length=60,null=True)
    # partner_name = models.CharField(max_length=60)
    image = models.ImageField(upload_to='parent/',null=True)
    partner_name = models.CharField(max_length=60,null=True)
    def __str__(self): 
        return str(self.name)

    def save_parent(self):
        self.save()

 
class Partners(models.Model):
    partner_name = models.CharField(max_length=60,null=True)
    description= models.CharField(max_length=60,null=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE, blank=True,null=True)
    email = models.CharField(max_length=60,null=True)
    partner_image = models.ImageField(upload_to='partner/',null=True)
    approved = models.BooleanField(default=False )
    phone= models.CharField(max_length=60,null=True)

    def __str__(self):
        return str(self.partner_name)
        
    def save_partner(self):
        self.save()

class Activities(models.Model):
    partner_name = models.ForeignKey(Partners, on_delete=models.CASCADE, blank=True,null=True)
    activity_name =models.CharField(max_length=60,null=True)
    description= models.CharField(max_length=60,null=True)
    activity_image = models.ImageField(upload_to='activity/',null=True ,blank=True)
    price=models.CharField(max_length=60,null=True)
    
    @classmethod
    def ge_all_act(cls):
        act = cls.objects.all().prefetch_related('comments_set')
        return act
    def __str__(self):
        return str(self.activity_name)
    def save_activity(self):
        self.save()

class Child(models.Model):
    names=models.CharField(max_length=60,null=True)
    age = models.IntegerField()
    parent = models.ForeignKey(Parents,on_delete=models.CASCADE, blank=True,null=True)
    activity_id = models.ForeignKey(Activities, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.names)

    def save_child(self):
        self.save()


class Comments(models.Model):
    comment_cont = models.CharField(max_length=120)
    commented_by = models.ForeignKey(Parents, on_delete=models.CASCADE, null=True)
    commented_act = models.ForeignKey(Activities, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return str(self.comment_cont)
    def save_comment(self):
        self.save()