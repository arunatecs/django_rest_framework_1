
from django.db import models

from django.contrib.auth.models import User
from organisation.models import Organisation
from audit_fields.models import AuditModelMixin
from django_currentuser.db.models import CurrentUserField
class borrower_group(AuditModelMixin,models.Model):
    org_id=models.ForeignKey(Organisation,on_delete=models.CASCADE, null=True, blank=True,related_name='org_id+')
    name = models.CharField(max_length=255, null=True, blank=True,)
    description = models.CharField(max_length=2000 , null=True, blank=True,)
    principal_due = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    created_by = CurrentUserField(related_name='created_by_bg',)
    updated_by = CurrentUserField(on_update=True,related_name='updated_by_bg',)
    
    class Meta(AuditModelMixin.Meta):
    
        pass 


   





    def __str__(self):
        return self.name

   
    
