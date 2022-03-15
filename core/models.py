from atexit import register
from pyexpat import model
from statistics import mode
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver 
from django.db.models.signals import post_save 
import uuid

class Students(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=20,null=True)
    reg_num=models.CharField(max_length=13,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    phone=models.CharField(max_length=10,unique=True)
    dob = models.DateField(null=True)
    mail = models.EmailField(unique=True)

    # token = models.UUIDField(primary_key=True,unique=False,default = uuid.uuid4,editable = True)
    token = models.CharField(max_length=50,unique=True,null=True)
    
    
    @receiver(post_save, sender=User) 
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Students.objects.create(user=instance)
    def __str__(self):
        return "{} ({})".format(self.name,self.user.username)

