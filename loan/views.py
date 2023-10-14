
from rest_framework import generics
from .serializer import loanSerializer
from .models import loan
from rest_framework.permissions import IsAuthenticated
class LoanListView(generics.ListCreateAPIView):

    queryset = loan.objects.all()
    serializer_class = loanSerializer
    name = 'loan-list'

    

    permission_classes = (
        IsAuthenticated,
    )
   
class loanDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = loan.objects.all()
    serializer_class = loanSerializer
    name = 'loan-detail'
    
    permission_classes = (
        IsAuthenticated,
    )
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(modified_by=self.request.user)

class loanDeleteView(generics.DestroyAPIView):
    queryset = loan.objects.all()
    serializer_class = loanSerializer      