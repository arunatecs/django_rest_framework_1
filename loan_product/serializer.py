from rest_framework import serializers

from loan_product.models import loan_product



class loan_productSerializer(serializers.ModelSerializer):
    
   
    class Meta:
        model = loan_product
        fields = (
            "id",
           
            "name",
            "description",
            "loandisk_id",
            "label",
            "created_by",
            "created",
            "modified",
            "updated_by",
            
        )
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)
