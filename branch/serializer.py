from rest_framework import serializers

from branch.models import branch



class branchSerializer(serializers.ModelSerializer):
    
   
    class Meta:
        model = branch
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

