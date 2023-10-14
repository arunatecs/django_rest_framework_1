from django.urls import path
from adjusted_loan_schedule import views

app_name = "api_adjusted_loan_schedule"

urlpatterns = [
    path("adjusted_loan_schedule", views.adjusted_loan_scheduleListView.as_view()),
    
]
