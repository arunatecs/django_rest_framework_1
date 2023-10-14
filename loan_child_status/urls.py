from django.urls import path
from loan_child_status import views
app_name = "api_loan_child_status"

urlpatterns = [
    path("loan_child_status", views.loan_child_statusListView.as_view()),
    
]
