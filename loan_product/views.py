
from rest_framework import generics
from .serializer import loan_productSerializer
from .models import loan_product
from rest_framework.permissions import IsAuthenticated

class Loan_productListView(generics.ListCreateAPIView):

    queryset = loan_product.objects.all()
    serializer_class = loan_productSerializer
    name = 'loan_product-list'

    
    permission_classes = (
        IsAuthenticated,
    )
    

class loanproductDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = loan_product.objects.all()
    serializer_class = loan_productSerializer
    name = 'loan_product-detail'
    
    permission_classes = (
        IsAuthenticated,
    )
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(modified_by=self.request.user)
   
class loanproductDeleteView(generics.DestroyAPIView):
	queryset = loan_product.objects.all()
	serializer_class = loan_productSerializer
     