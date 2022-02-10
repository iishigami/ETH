from django.urls import path, include

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('piechart/', pie, name='pie'),
    path('linechart/', line, name='line'),
    
]
