
from django.db import models

from django.contrib.auth.models import User
from loan.models import loan
from audit_fields.models import AuditModelMixin
from django_currentuser.db.models import CurrentUserField
class repayment(AuditModelMixin,models.Model):
    repayment_id = models.CharField(max_length=45)
    LoanId=models.ForeignKey(loan,on_delete=models.CASCADE, null=True, blank=True,related_name='loan')
    #org_id=models.ForeignKey(Organisation,on_delete=models.CASCADE, null=True, blank=True,related_name='org_id++')
    branch_id = models.CharField(max_length=255)
    repayment_amount = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    loan_repayment_method_id = models.CharField(max_length=45, null=True, blank=True,) 
    repayment_collected_date = models.CharField(max_length=45, null=True, blank=True,) 
    collector_id = models.CharField(max_length=45, null=True, blank=True,) 
    loan_do_not_adjust_remaining_pro_rata = models.CharField(max_length=45, null=True, blank=True,) 
    repayment_adjust_remaining_schedule = models.CharField(max_length=45, null=True, blank=True,) 
    repayment_manual_composition = models.CharField(max_length=45, null=True, blank=True,) 
    principal_repayment_amount= models.DecimalField(default=0, max_digits=8, decimal_places=2)
    interest_repayment_amount= models.DecimalField(default=0, max_digits=8, decimal_places=2)
    fees_repayment_amount = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    penalty_repayment_amount = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    repayment_description = models.CharField(max_length=45, null=True, blank=True,)  
    
    created_by = CurrentUserField(related_name='created_by_repay',)
    updated_by = CurrentUserField(on_update=True,related_name='updated_by_repay',)
    
    class Meta(AuditModelMixin.Meta):
    
        pass 
   





    def __str__(self):
        return self.repayment_id

   
    
