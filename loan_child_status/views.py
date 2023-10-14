
from rest_framework import generics
from .serializer import loan_child_statusSerializer
from .models import loan_child_status
from rest_framework.permissions import IsAuthenticated
class loan_child_statusListView(generics.ListCreateAPIView):

    queryset = loan_child_status.objects.all()
    serializer_class = loan_child_statusSerializer
    name = 'loan_child_status-list'

    
    permission_classes = (
        IsAuthenticated,
    )
    

    