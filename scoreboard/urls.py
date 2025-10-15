from django.contrib import admin
from django.urls import path
from django.urls import include 
from rest_framework import routers


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("registration.urls")),
    path("api/", include("main_board.urls"))
    ]
