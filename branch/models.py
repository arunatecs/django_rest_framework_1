
from django.db import models

from django.contrib.auth.models import User
from organisation.models import Organisation
from audit_fields.models import AuditModelMixin
from django_currentuser.db.models import CurrentUserField
class branch(AuditModelMixin,models.Model):
    loandisk_id = models.CharField(max_length=50,blank=True)
    org_id=models.ForeignKey(Organisation,on_delete=models.CASCADE, null=True, blank=True,related_name='org_id++')
    label = models.CharField(max_length=255,blank=True)
    name = models.CharField(max_length=255, null=True, blank=True,)
    description = models.CharField(max_length=2000 , null=True, blank=True,)
    created_by = CurrentUserField(related_name='created_by_branch',)
    updated_by = CurrentUserField(on_update=True,related_name='updated_by_branch',)
    
    class Meta(AuditModelMixin.Meta):
    
        pass 
    




    def __str__(self):
        return self.label

   
    
