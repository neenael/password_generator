from django.urls import path
from .views import PasswordMake

app_name = 'password_app'
urlpatterns = [
    path('', PasswordMake.as_view(), name='password_make')
]
