
from rest_framework import generics
from .serializer import branchSerializer
from .models import branch
from rest_framework.permissions import IsAuthenticated
class branchListView(generics.ListCreateAPIView):

    queryset = branch.objects.all()
    serializer_class = branchSerializer
    name = 'branch-list'

    permission_classes = (
        IsAuthenticated,
    )
class branchDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = branch.objects.all()
    serializer_class = branchSerializer
    name = 'branch-detail'
    
    permission_classes = (
        IsAuthenticated,
    )
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(modified_by=self.request.user)
   

class branchDeleteView(generics.DestroyAPIView):
    queryset = branch.objects.all()
    serializer_class = branchSerializer