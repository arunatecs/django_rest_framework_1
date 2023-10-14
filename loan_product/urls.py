from django.urls import path
from loan_product import views

app_name = "api_loan_product"

urlpatterns = [
    path("loan_product", views.Loan_productListView.as_view()),
    path('loanproduct/<int:pk>',views.loanproductDetail.as_view(),name=views.loanproductDetail.name),
    path('loanproduct/<int:pk>/', views.loanproductDeleteView.as_view(), name='loanproduct-delete'),
]
