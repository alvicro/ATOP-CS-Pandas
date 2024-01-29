from django.urls import path
from .views import display_xls, draw

urlpatterns = [
    path('', display_xls),
    path('draw/', draw)
]
