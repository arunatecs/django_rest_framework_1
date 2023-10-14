from django.urls import path
from loan_repayment_method import views

app_name = "api_loan_repayment_method"

urlpatterns = [
    path("loan_repayment_method", views.loan_repayment_methodListView.as_view()),
    
]
