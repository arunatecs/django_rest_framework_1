
from rest_framework import generics
from .serializer import adjusted_loan_scheduleSerializer
from .models import adjusted_loan_schedule
from rest_framework.permissions import IsAuthenticated
class adjusted_loan_scheduleListView(generics.ListCreateAPIView):

    queryset = adjusted_loan_schedule.objects.all()
    serializer_class = adjusted_loan_scheduleSerializer
    name = 'adjusted_loan_schedule-list'

    

    permission_classes = (
        IsAuthenticated,
    )
   
