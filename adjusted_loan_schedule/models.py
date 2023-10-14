
from django.db import models

from django.contrib.auth.models import User
from organisation.models import Organisation
from audit_fields.models import AuditModelMixin
from django_currentuser.db.models import CurrentUserField

class adjusted_loan_schedule(AuditModelMixin,models.Model):
    loan_id = models.CharField(max_length=45)
    org_id=models.ForeignKey(Organisation,on_delete=models.CASCADE, null=True, blank=True,related_name='org_id+')
    branch_id = models.CharField(max_length=255)
    hash = models.CharField(max_length=45, null=True, blank=True,)
    date = models.CharField(max_length=45, null=True, blank=True,)
    description = models.CharField(max_length=45, null=True, blank=True,) 
    principal = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    interest= models.DecimalField(default=0, max_digits=8, decimal_places=2)
    fees= models.DecimalField(default=0, max_digits=8, decimal_places=2)
    penalty = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    due = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    pending_due = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    total_due= models.DecimalField(default=0, max_digits=8, decimal_places=2)
    principal_due = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    created_by = CurrentUserField(related_name='created_by_als',)
    updated_by = CurrentUserField(on_update=True,related_name='updated_by_als',)
    
    class Meta(AuditModelMixin.Meta):
    
        pass 





    def __str__(self):
        return self.borrower_id

   
    
