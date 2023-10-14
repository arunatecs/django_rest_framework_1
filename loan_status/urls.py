from django.urls import path
from loan_status import views

app_name = "api_loan_status"

urlpatterns = [
    path("loan_status", views.loan_statusListView.as_view()),
    
]
