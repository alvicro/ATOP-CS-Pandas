from django.urls import path
from .views import *

urlpatterns = [
    path('', display_xls),
    path('draw/', draw),
    path('groundwater_levels/', groundwater_levels),
    path('atmospheric_pressure/', pressure),
    path('precipitation/', precipitation),
    path('air_temperature/', air_temperature),
    path('Combined_graph_of_h-x-P-t/', hxpt),
    path('deep_neural_network/', show_links),
    path('neural_networks_in_hydrological_forecasts/', show_pictures),
    path('lack_of_correlation/', show_graphics),
]