from django.urls import path
from MysoreApp import views as m

urlpatterns=[
    path('vijayanagar',m.corona_vijayanagar),
    path('kdroad',m.corona_kdroad),
    path('rknagar',m.corona_rknagar),
]