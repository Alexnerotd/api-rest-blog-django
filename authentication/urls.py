from django.urls import path
from .views import Login, Registration



urlpatterns = [
    path("login/", Login.as_view(), name='login'),
    path("registration/", Registration.as_view(), name='registration'),
]
