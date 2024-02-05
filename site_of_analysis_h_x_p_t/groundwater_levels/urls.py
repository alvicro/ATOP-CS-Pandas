from django.urls import path
from .views import display_xls, draw, groundwater_levels

urlpatterns = [
    path('', display_xls),
    path('draw/', draw),
    path('groundwater_levels/', groundwater_levels)
]
