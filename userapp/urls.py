from django.urls import path
from rest_framework.authtoken import views
from userapp.views import registration_view

urlpatterns = [
    path('login/', views.obtain_auth_token, name='login'),
    path('register/', registration_view, name='register'),
]
