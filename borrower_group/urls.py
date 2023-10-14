from django.urls import path
from borrower_group import views

app_name = "api_borrowergroup"

urlpatterns = [
    path("borrower_group", views.borrower_groupListView.as_view()),
    
]
