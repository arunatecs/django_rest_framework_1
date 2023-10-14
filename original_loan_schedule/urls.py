from django.urls import path
from original_loan_schedule import views

app_name = "api_original_loan_schedule"

urlpatterns = [
    path("original_loan_schedule", views.original_loan_scheduleView.as_view()),
    
]
