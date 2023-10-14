
from rest_framework import generics
from .serializer import borrowerSerializer
from .models import borrower
from rest_framework.permissions import IsAuthenticated
class borrowerList(generics.ListCreateAPIView):

    queryset = borrower.objects.all()
    serializer_class = borrowerSerializer
    name = 'borrower-list'

    filter_fields = (
        'borrower_firstname',
    )
    search_fields = (
        '^borrower_firstname',
    )
    ordering_fields = (
        'borrower_firstname',
    )

    permission_classes = (
        IsAuthenticated,
    )
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(modified_by=self.request.user)

class borrowerDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = borrower.objects.all()
    serializer_class = borrowerSerializer
    name = 'borrower-detail'
    
    permission_classes = (
        IsAuthenticated,
    )
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(modified_by=self.request.user)