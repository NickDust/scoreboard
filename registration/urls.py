from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.RegisterUserView.as_view(), name='register')]