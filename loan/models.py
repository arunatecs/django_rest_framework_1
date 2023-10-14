#import arrow
from django.db import models
#from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from audit_fields.models import AuditModelMixin
from django_currentuser.db.models import CurrentUserField
from borrower.models import borrower
class loan(AuditModelMixin,models.Model):
   
    loan_id = models.CharField(max_length=45, null=True, blank=True,)
    borrower_id =models.ForeignKey(borrower,on_delete=models.CASCADE, null=True, blank=True,related_name='borrower')
    loan_product_id = models.CharField(max_length=45, null=True, blank=True,)
    loan_application_id = models.CharField(max_length=45, null=True, blank=True,)
    loan_disbursed_by_id = models.CharField(max_length=45, null=True, blank=True,)
    loan_principal_amount = models.CharField(max_length=45, null=True, blank=True,)
    loan_released_date = models.CharField(max_length=45, null=True, blank=True,)
    loan_interest_method = models.CharField(max_length=45, null=True, blank=True,)
    loan_interest_type = models.CharField(max_length=45, null=True, blank=True,)
    loan_interest_period = models.CharField(max_length=45, null=True, blank=True,)
    loan_interest = models.CharField(max_length=45, null=True, blank=True,)
    loan_duration_period = models.CharField(max_length=45, null=True, blank=True,)
    loan_duration_type = models.CharField(max_length=45, null=True, blank=True,)
    loan_duration = models.CharField(max_length=45, null=True, blank=True,)
    loan_payment_scheme_id = models.CharField(max_length=45, null=True, blank=True,)
    loan_num_of_repayments = models.CharField(max_length=45, null=True, blank=True,)
    loan_decimal_places = models.CharField(max_length=45, null=True, blank=True,)
    loan_interest_start_date = models.CharField(max_length=45, null=True, blank=True,)
    loan_fees_pro_rata = models.CharField(max_length=45, null=True, blank=True,)
    loan_do_not_adjust_remaining_pro_rata = models.CharField(max_length=45, null=True, blank=True,)
    loan_first_repayment_pro_rata = models.CharField(max_length=45, null=True, blank=True,)
    loan_first_repayment_date = models.CharField(max_length=45, null=True, blank=True,)
    first_repayment_amount = models.CharField(max_length=45, null=True, blank=True,)
    last_repayment_amount = models.CharField(max_length=45, null=True, blank=True,)
    loan_override_maturity_date = models.CharField(max_length=45, null=True, blank=True,)
    override_each_repayment_amount = models.CharField(max_length=45, null=True, blank=True,)
    loan_interest_each_repayment_pro_rata = models.CharField(max_length=45, null=True, blank=True,)
    loan_interest_schedule = models.CharField(max_length=45, null=True, blank=True,)
    loan_principal_schedule = models.CharField(max_length=45, null=True, blank=True,)
    loan_balloon_repayment_amount = models.CharField(max_length=45, null=True, blank=True,)
    automatic_payments = models.CharField(max_length=45, null=True, blank=True,)
    payment_posting_period = models.CharField(max_length=45, null=True, blank=True,)
    total_amount_due = models.CharField(max_length=45, null=True, blank=True,)
    balance_amount = models.CharField(max_length=45, null=True, blank=True,)
    due_date = models.CharField(max_length=45, null=True, blank=True,)
    total_paid = models.CharField(max_length=45, null=True, blank=True,)
    child_status_id = models.CharField(max_length=45, null=True, blank=True,)
    loan_fee_schedule_3951 = models.CharField(max_length=45, null=True, blank=True,)
    loan_fee_id_3951 = models.CharField(max_length=45, null=True, blank=True,)
    
    class Meta(AuditModelMixin.Meta):
    
      pass 
    created_by = CurrentUserField(related_name='created_by+',)
    updated_by = CurrentUserField(on_update=True,related_name='updated_by+',)
    
    
    
    





    def __str__(self):
        return self.loan_id

   
    
