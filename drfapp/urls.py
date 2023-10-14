"""drfapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,  include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from usersapi.views import APILogoutView, ProfileView

urlpatterns = [
    # gastonmiller
    path('admin/', admin.site.urls),
    #path('', include('droneapi.urls')),
    #path('', include('organisation.urls')),
     path('', include('loan.urls'),name ="loan"),
     path('', include('original_loan_schedule.urls'),name ="original_loan_schedule"),
     path('', include('adjusted_loan_schedule.urls'),name ="adjusted_loan_schedule"),
     path('', include('organisation.urls'),name ="organisation"),
     path('', include('borrower.urls'),name="borrower"),
    path('', include('borrower_group.urls'),name="borrower_group"),
    path('', include('branch.urls'),name="branch"),  
     path('', include('repayment.urls'),name="repayment"),
     path('', include('loan_child_status.urls'),name="loan_child_status"), 
      path('', include('loan_product.urls'),name="loan_product"), 
      path('', include('loan_repayment_method.urls'),name="loan_repayment_method"), 
        path('', include('loan_status.urls'),name="loan_status"), 
    path('api-auth/', include('rest_framework.urls')) ,

    #JM djangorestframework-simplejwt
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/logout_token/', APILogoutView.as_view(), name='logout_token'),

    path('user/me/', ProfileView.as_view(), name='me'),

    path('users/', include('usersapi.urls')),

    

]
