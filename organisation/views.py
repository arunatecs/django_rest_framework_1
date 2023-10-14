
from rest_framework import generics
from .serializer import OrganisationSerializer
from .models import Organisation
from rest_framework.permissions import IsAuthenticated
class OrganisationListView(generics.ListCreateAPIView):

    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer
    name = 'organisation-list'

    filter_fields = (
        'name',
    )
    search_fields = (
        '^name',
    )
    ordering_fields = (
        'name',
    )

    permission_classes = (
        IsAuthenticated,
    )

    