from rest_framework import serializers

#For User Serializer
from django.contrib.auth.models import User

from rest_framework import serializers, status
from usersapi.models import *

'''
https://www.freecodecamp.org/news/nested-relationships-in-serializers-for-onetoone-fields-in-django-rest-framework-bdb4720d81e6/
'''

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class ProfileSerializer(serializers.ModelSerializer):
    """
    A profile serializer to return the user and profile details
    """
    #user = UserSerializer(required=True)
    first_name = serializers.CharField(read_only=True, source="user.first_name")
    last_name = serializers.CharField(read_only=True, source="user.last_name")
    email = serializers.CharField(read_only=True, source="user.email")

    class Meta:
        model = Profile
        fields = ('id','first_name', 'last_name','email', 'phone_number', 'is_email_confirmed', 
                  'is_phone_number_confirmed','is_2fa_enabled', 'uuid')


    
    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details of student
        :return: returns a successfully created student record
        """
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        profile, created = Profile.objects.update_or_create(user=user,
                            subject_major=validated_data.pop('subject_major'))
        return profile
    