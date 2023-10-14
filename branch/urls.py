from django.urls import path
from branch import views

app_name = "api_branch"

urlpatterns = [
    path("branch", views.branchListView.as_view()),
    path('branch/<int:pk>',views.branchDetail.as_view(),name=views.branchDetail.name),
    path('branch/<int:pk>/', views.branchDeleteView.as_view(), name='branch-delete'),
]
