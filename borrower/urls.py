from django.urls import path
from borrower import views

app_name = "api_borrower"

urlpatterns = [
   
    path('borrower',
        views.borrowerList.as_view(),
        name=views.borrowerList.name),
    path('borrower/<int:pk>',
        views.borrowerDetail.as_view(),
        name=views.borrowerDetail.name),
]
