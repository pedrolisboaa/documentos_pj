from django.urls import path
from .views import index


app_name = 'contas'

urlpatterns = [
    path('', index, name="index"),
]
