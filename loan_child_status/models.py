
from django.db import models
from audit_fields.models import AuditModelMixin
from django_currentuser.db.models import CurrentUserField 
from django.contrib.auth.models import User
from organisation.models import Organisation
class loan_child_status(AuditModelMixin,models.Model):
    loandisk_id = models.CharField(max_length=50)
    org_id=models.ForeignKey(Organisation,on_delete=models.CASCADE, null=True, blank=True,related_name='org_id+')
    label = models.CharField(max_length=255)
    name = models.CharField(max_length=255, null=True, blank=True,)
    description = models.CharField(max_length=2000, null=True, blank=True,)
    class Meta(AuditModelMixin.Meta):
    
      pass 
    created_by = CurrentUserField(related_name='created_by_loan_child_status',)
    updated_by = CurrentUserField(on_update=True,related_name='updated_byloan_child_status',)






    def __str__(self):
        return self.label

   
    
