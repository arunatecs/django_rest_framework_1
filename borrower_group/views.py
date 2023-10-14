
from rest_framework import generics
from .serializer import borrower_groupSerializer
from .models import borrower_group
from rest_framework.permissions import IsAuthenticated
class borrower_groupListView(generics.ListCreateAPIView):

    queryset = borrower_group.objects.all()
    serializer_class = borrower_groupSerializer
    name = 'borrowergroup-list'

    
    permission_classes = (
        IsAuthenticated,
    )
    

    