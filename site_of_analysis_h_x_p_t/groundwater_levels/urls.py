from django.urls import path
from .views import display_xls, draw, groundwater_levels, pressure, precipitation, air_temperature, hxpt

urlpatterns = [
    path('', display_xls),
    path('draw/', draw),
    path('groundwater_levels/', groundwater_levels),
    path('atmospheric_pressure/', pressure),
    path('precipitation/', precipitation),
    path('air_temperature/', air_temperature),
    path('Combined_graph_of_h-x-P-t', hxpt)
]
