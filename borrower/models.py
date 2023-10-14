#import arrow
from django.db import models
#from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from  organisation.models import Organisation
from django.conf import settings
from audit_fields.models import AuditModelMixin
#from django_currentuser.middleware import ( get_current_user, get_current_authenticated_user)

from django_currentuser.db.models import CurrentUserField
  
class borrower(AuditModelMixin,models.Model):
    
    borrower_id = models.CharField(max_length=45)

    org_id=models.ForeignKey(Organisation,on_delete=models.CASCADE, null=True, blank=True,related_name='org_id+')
    branch_id = models.CharField(max_length=255)
    borrower_country = models.CharField(max_length=45, null=True, blank=True,)
    borrower_fullname = models.CharField(max_length=45, null=True, blank=True,) 
    borrower_firstname = models.CharField(max_length=45, null=True, blank=True,) 
    borrower_lastname = models.CharField(max_length=45, null=True, blank=True,) 
    borrower_business_name = models.CharField(max_length=45, null=True, blank=True,) 
    borrower_unique_number = models.CharField(max_length=45, null=True, blank=True,) 
    borrower_gender = models.CharField(max_length=45, null=True, blank=True,) 
    borrower_title = models.CharField(max_length=45, null=True, blank=True,) 
    borrower_mobile = models.CharField(max_length=45, null=True, blank=True,) 
    borrower_email = models.CharField(max_length=45, null=True, blank=True,) 
    borrower_dob = models.CharField(max_length=45, null=True, blank=True,) 
    borrower_address = models.CharField(max_length=45, null=True, blank=True,) 
    borrower_city = models.CharField(max_length=45, null=True, blank=True,) 
    borrower_province = models.CharField(max_length=45, null=True, blank=True,) 
    borrower_zipcode = models.CharField(max_length=45, null=True, blank=True,) 
    borrower_landline = models.CharField(max_length=45, null=True, blank=True,) 
    borrower_working_status = models.CharField(max_length=45, null=True, blank=True,) 
    borrower_credit_score = models.CharField(max_length=45, null=True, blank=True,) 
    borrower_description = models.CharField(max_length=45, null=True, blank=True,) 
    borrower_access_ids = models.CharField(max_length=45, null=True, blank=True,) 
    borrower_photo = models.CharField(max_length=45, null=True, blank=True,)
    created_by = CurrentUserField(related_name='created_by',)
    updated_by = CurrentUserField(on_update=True,related_name='updated_by',)
    class Meta(AuditModelMixin.Meta):
    
        pass 
  
    #createdat = models.DateTimeField(auto_now_add=True)
   
    #modifiedat = models.DateTimeField(auto_now=True)
    #createdby = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='created_by', blank=True, null=True)
    #modifiedby = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='updated_by', blank=True, null=True)"""
    
   





    def __str__(self):
        return self.borrower_id

   
    
