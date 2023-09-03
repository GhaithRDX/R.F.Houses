from django.urls import path , include
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('house/', views.HouseView_List),
    
    path('house/<int:id1>', views.HouseView_pk),
    
    path('api-auth', include('rest_framework.urls')),
    
    path('api-token-auth', obtain_auth_token),


]