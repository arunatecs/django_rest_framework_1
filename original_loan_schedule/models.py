#import arrow
from django.db import models
#from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from organisation.models import Organisation
from audit_fields.models import AuditModelMixin
from django_currentuser.db.models import CurrentUserField
class original_loan_schedule(AuditModelMixin,models.Model):
    loan_id = models.CharField(max_length=255)
    """
    org_id=models.ForeignKey(Organisation,on_delete=models.CASCADE, null=True, blank=True,related_name='org_id+')
    branch_id = models.CharField(max_length=255)
    date = models.CharField(max_length=45, null=True, blank=True,)
    description = models.CharField(max_length=45, null=True, blank=True,) 
    principal = models.DecimalField(default=0, max_digits=8, decimal_places=2)

    interest= models.DecimalField(default=0, max_digits=8, decimal_places=4)
    fees= models.DecimalField(default=0, max_digits=8, decimal_places=2)
    penalty = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    due = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    total_due= models.DecimalField(default=0, max_digits=8, decimal_places=2)
    principal_amount = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    emi = models.DecimalField(default=0, max_digits=10, decimal_places=4)"""
    principal =models.CharField(max_length=45)
    interest=models.CharField(max_length=45)
    total_payment= models.CharField(max_length=45)
    balance = models.CharField(max_length=45)
    loan_paid_date =models.CharField(max_length=45)
    
    loan_principal =models.CharField(max_length=45)
    loan_interest =models.DecimalField(default=0, max_digits=8, decimal_places=4)
    emi =models.CharField(max_length=45)
    
    created_by = CurrentUserField(related_name='createdby_ols',)
    updated_by = CurrentUserField(on_update=True,related_name='updated_by_ols',)
    class Meta(AuditModelMixin.Meta):
    
      pass 

    





    def __str__(self):
        return self.loan_id

   
    
