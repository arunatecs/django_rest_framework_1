from django.urls import path
from . import views



urlpatterns = [

    path('profiles/',
        views.UserProfileListGenView.as_view(),
        name=views.UserProfileListGenView.name),

    path('profiles/<int:pk>',
        views.UserProfileDetailGenView.as_view(),
        name=views.UserProfileDetailGenView.name),

]