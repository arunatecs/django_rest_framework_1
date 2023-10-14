from rest_framework import serializers

from adjusted_loan_schedule.models import adjusted_loan_schedule



class adjusted_loan_scheduleSerializer(serializers.ModelSerializer):
    
   
    class Meta:
        model = adjusted_loan_schedule
        fields = (
            "id",
            "loan_id",
            "org_id",  
            "branch_id", 
            "hash",
            "date",  
            "description",  
            "principal",  
            "interest" , 
            "fees",  
            "penalty", 
            "due", 
            "pending_due", 
            "total_due", 
            "principal_due",
           
            "created_by",
            "created",
            "updated_by",
            "modified",
            
        )


