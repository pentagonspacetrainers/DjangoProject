from django.urls import path
from BangaloreApp import views as b

urlpatterns=[
    path('vijayanagar',b.corona_vijayanagar),
    path('jayanagar',b.corona_jayanagar),\
    path('rajajinagar',b.corona_rajajinagar),
]