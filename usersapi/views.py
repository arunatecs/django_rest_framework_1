from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth.models import User

from usersapi.serializers import *
from usersapi.models import *
#from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class APILogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        if self.request.data.get('all'):
            token: OutstandingToken
            for token in OutstandingToken.objects.filter(user=request.user):
                _, _ = BlacklistedToken.objects.get_or_create(token=token)
            return Response({"status": "OK, goodbye, all refresh tokens blacklisted"})
        refresh_token = self.request.data.get('refresh_token')
        token = RefreshToken(token=refresh_token)
        token.blacklist()
        return Response({"status": "OK, goodbye"})

'''
Read-Only data for display

https://stackoverflow.com/questions/15770488/return-the-current-user-with-django-rest-framework
''' 
class ProfileView(APIView):

    #queryset = User.objects.all()
    #serializer_class = UserSerializer
    name = 'user-detail'

    permission_classes = (
         IsAuthenticated,
        )
    
    def get(self, request):

        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None (returns access token)
            'first_name' : str(request.user.first_name),
            'phome_number': str(request.user.profile.phone_number) # 
        }
        return Response(content)
        #serializer = UserSerializer(request.user)
        #print('data',test)


'''
For List 
https://www.freecodecamp.org/news/nested-relationships-in-serializers-for-onetoone-fields-in-django-rest-framework-bdb4720d81e6/
'''

class UserProfileListView(APIView):
    """
    A class based view for fetching profile records  
    """

    permission_classes = (
         IsAuthenticated,
        )
    def get(self, format=None):
        """
        Get all the profile records
        :param format: Format of the profile records to return to
        :return: Returns a list of profile records
        """
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)


class UserProfileDetailView(APIView):
    """
    A class based view for creating a profile record 
    https://www.freecodecamp.org/news/nested-relationships-in-serializers-for-onetoone-fields-in-django-rest-framework-bdb4720d81e6/

    """
  
    def post(self, request):
        """
        Create a profile  record
        :param format: Format of the profile records to return to
        :param request: Request object for creating profile
        :return: Returns a profile record
        """
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)
    

   
class UserProfileListGenView(generics.ListCreateAPIView):
    """
    A class based view for fetching profile records and creating
    GastonMillar Alternative to    UserProfileListView
    """

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = 'profile-list'
  
    ordering_fields = (
            'user.first_name',
          
        )
    
    permission_classes = (
        IsAuthenticated,
    )

    
class UserProfileDetailGenView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = 'profile-detail'

    permission_classes = (
        IsAuthenticated,
    )
