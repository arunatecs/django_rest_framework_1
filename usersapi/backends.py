from django.db import models


from django.contrib.auth.backends import ModelBackend, UserModel
from django.contrib.auth import get_user_model
from django.db.models import Q

'''
django-login-with-email
https://stackoverflow.com/questions/37332190/django-login-with-email
'''



UserModel = get_user_model()

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try: #to allow authentication through phone number or any other field, modify the below statement
            #user = UserModel.objects.get(Q(username__iexact=username) | Q(email__iexact=username)) # JM
            #Use email in username
            user = UserModel.objects.get( Q(email__iexact=username))
        except UserModel.DoesNotExist:
            UserModel().set_password(password)
        except UserModel.MultipleObjectsReturned:
            return UserModel.objects.filter(email=username).order_by('id').first()
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user

    def get_user(self, user_id):
        try:
            user = UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None

        return user if self.user_can_authenticate(user) else None