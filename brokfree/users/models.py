from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=30,blank=True,null=True)
    last_name=models.CharField(max_length=30,blank=True,null=True)
    mobile=models.CharField(max_length=10,blank=False,null=False)
    date=models.CharField(max_length=20,blank=True,null=True)
    email_confirmed=models.BooleanField(default=False)
    def __str__(self):
        return self.user.username

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
