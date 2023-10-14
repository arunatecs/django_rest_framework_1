from django.urls import path
from organisation import views

app_name = "api_organisation"

urlpatterns = [
    path("org", views.OrganisationListView.as_view()),
    
]
