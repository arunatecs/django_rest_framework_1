from django.urls import path
from loan import views

app_name = "api_loan"

urlpatterns = [
    path("loan", views.LoanListView.as_view()),
    path('loan/<int:pk>',
        views.loanDetail.as_view(),
        name=views.loanDetail.name),
    path('loan/<int:pk>/', views.loanDeleteView.as_view(), name='loan-delete'),
    
]
