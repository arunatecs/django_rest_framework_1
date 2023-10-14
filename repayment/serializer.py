from rest_framework import serializers

from repayment.models import repayment



class repaymentSerializer(serializers.ModelSerializer):
    
   
    class Meta:
        model = repayment
        fields = (
            "id",
            "repayment_id",
            "LoanId",  
            "branch_id", 
            "repayment_amount",  
            "loan_repayment_method_id",  
            "repayment_collected_date",  
            "collector_id" , 
            "loan_do_not_adjust_remaining_pro_rata",  
            "repayment_adjust_remaining_schedule", 
            "repayment_manual_composition",  
            "principal_repayment_amount", 
            "interest_repayment_amount",
            "fees_repayment_amount",  
            "penalty_repayment_amount", 
            "repayment_description",
            "created_by",
            "created",
            "modified",
            "updated_by",
            
        )
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)


