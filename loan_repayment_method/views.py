
from rest_framework import generics
from .serializer import loan_repayment_methodSerializer
from .models import loan_repayment_method
from rest_framework.permissions import IsAuthenticated
class loan_repayment_methodListView(generics.ListCreateAPIView):

    queryset = loan_repayment_method.objects.all()
    serializer_class = loan_repayment_methodSerializer
    name = 'loan_repayment_method-list'

    
    

    permission_classes = (
        IsAuthenticated,
    )

    

    