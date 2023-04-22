#เลขาหน้าห้อง
from django.urls import path
from .views import Homepage


urlpatterns = [
    path('',Homepage),  #local host:8000
]
