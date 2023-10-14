from rest_framework import serializers

from borrower_group.models import borrower_group



class borrower_groupSerializer(serializers.ModelSerializer):
    
   
    class Meta:
        model = borrower_group
        fields = (
            "id",
            "org_id",
            "name",
            "description",
            "created_by",
            "created",
            "updated_by",
            "modified",
        )


    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)