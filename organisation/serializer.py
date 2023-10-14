from rest_framework import serializers

from organisation.models import Organisation



class OrganisationSerializer(serializers.ModelSerializer):
    
   
    class Meta:
        model = Organisation
        fields = (
            "id",
           
            "name",
            "description",
            "created_by",
            "created",
            "modified",
            "updated_by",
        )

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)
