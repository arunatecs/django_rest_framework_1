#import arrow
from django.db import models
#from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
#from audit_fields.model_mixins import AuditUuidModelMixin
from audit_fields.models import AuditModelMixin
#from simple_history.models import HistoricalRecords
from django_currentuser.db.models import CurrentUserField
#from field_audit import audit_fields
#@audit_fields("description")
class Organisation(AuditModelMixin, models.Model):

   #history = HistoricalRecords()


    
   name = models.CharField(max_length=255)
   description = models.CharField(max_length=2000)
   created_by = CurrentUserField(related_name='created_by_org',)
   updated_by = CurrentUserField(on_update=True,related_name='updated_by_org',)
    
   class Meta(AuditModelMixin.Meta):
    
        pass    



def __str__(self):
    return self.name

   
    
