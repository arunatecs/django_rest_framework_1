
from rest_framework import generics
from .serializer import original_loan_scheduleSerializer
from original_loan_schedule.models import original_loan_schedule
import pandas as pd 
from rest_framework.permissions import IsAuthenticated
class original_loan_scheduleView(generics.ListCreateAPIView):

  
    queryset = original_loan_schedule.objects.all()
    
    serializer_class = original_loan_scheduleSerializer

    permission_classes = (
        IsAuthenticated,
    )