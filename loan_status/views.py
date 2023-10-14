
from rest_framework import generics
from .serializer import loan_statusSerializer
from .models import loan_status
from rest_framework.permissions import IsAuthenticated
class loan_statusListView(generics.ListCreateAPIView):

    queryset = loan_status.objects.all()
    serializer_class = loan_statusSerializer
    name = 'loan_status-list'

    permission_classes = (
        IsAuthenticated,
    )

    

    