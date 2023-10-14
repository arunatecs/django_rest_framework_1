

# Create your models here.

'''
django-auth-user-with-unique-email

Make email field unique
https://stackoverflow.com/questions/5773970/django-auth-user-with-unique-email

extending user
https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#abstractuser
'''

import uuid
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



User.email = models.EmailField(("email address"),  unique=True)


#from django.contrib.auth.models import User
'''
Extend the user Model and add more fields
'''

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    is_email_confirmed = models.BooleanField(default=False)
    is_phone_number_confirmed = models.BooleanField(default=False)
    is_2fa_enabled = models.BooleanField(default=False)
    uuid = models.UUIDField(
        #primary_key = True,
        default = uuid.uuid4,
        editable = False)
    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()    
