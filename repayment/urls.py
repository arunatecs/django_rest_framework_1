from django.urls import path
from repayment import views

app_name = "api_repayment"

urlpatterns = [
    path("repayment", views.repaymentListView.as_view()),
    
]
