from django.urls import path
from .views import diplay_xls

urlpatterns = [
    path('', diplay_xls)
]
