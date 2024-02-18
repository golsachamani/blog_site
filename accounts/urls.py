from django.urls import path
from .views import *
urlpatterns = [
    path('signUP/', SignUpView.as_view(), name= 'signup')
]
   