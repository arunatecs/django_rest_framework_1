from rest_framework import serializers

from original_loan_schedule.models import original_loan_schedule



class original_loan_scheduleSerializer(serializers.ModelSerializer):
    
   
    class Meta:
        model = original_loan_schedule
        fields = (
            "id",
            "loan_id",
            "org_id",  
            "branch_id", 
            "date",  
            "description",  
            "principal",  
            "interest" , 
            "fees",  
            "penalty", 
            "due",  
            "total_due", 
            "principal_amount",
            "emi",
            "created_by",
            "created",
            "modified",
            "updated_by",
            
        )


    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)