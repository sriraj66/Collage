from atexit import register
from pyexpat import model
from statistics import mode
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver 
from django.db.models.signals import post_save 

class Students(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    reg_num=models.CharField(max_length=13,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    phone=models.CharField(max_length=10,unique=True)
    dob = models.DateField()
    mail = models.EmailField(unique=True)

    @receiver(post_save, sender=User) 
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Students.objects.create(user=instance)
