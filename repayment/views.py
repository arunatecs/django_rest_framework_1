
from rest_framework import generics
from .serializer import repaymentSerializer
from .models import repayment
from rest_framework.permissions import IsAuthenticated
class repaymentListView(generics.ListCreateAPIView):

    queryset = repayment.objects.all()
    serializer_class = repaymentSerializer
    name = 'repayment-list'

    

    permission_classes = (
        IsAuthenticated,
    )
   
