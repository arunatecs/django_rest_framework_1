from rest_framework import serializers

from borrower.models import borrower



class borrowerSerializer(serializers.ModelSerializer):
    #createdby = serializers.StringRelatedField(default=serializers.CurrentUserDefault(), read_only=True)
    #modifiedby = serializers.StringRelatedField(default=serializers.CurrentUserDefault(), read_only=True)
   
    class Meta:
        model = borrower
        fields = [
            "id",
            "borrower_id",
            "borrower_country",  
            "borrower_fullname", 
            "borrower_firstname",  
            "borrower_lastname",  
            "borrower_business_name",  
            "borrower_unique_number" , 
            "borrower_gender",  
            "borrower_title", 
            "borrower_mobile",  
            "borrower_email", 
            "borrower_dob",
            "borrower_address",  
            "borrower_city", 
            "borrower_province" ,
            "borrower_zipcode", 
            "borrower_landline",  
            "borrower_working_status", 
            "borrower_credit_score", 
            "borrower_description", 
            "borrower_access_ids",  
            "borrower_photo",
            "created_by",
            "created",
            "modified",
            "updated_by",
            
        ]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)
