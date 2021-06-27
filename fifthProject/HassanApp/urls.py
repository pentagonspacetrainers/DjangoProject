from django.urls import path
from HassanApp import views as h

urlpatterns=[
    path('satyamangala',h.corona_satyamangala),
    path('crpatna',h.corona_crpatna),
    path('arsikere',h.corona_arsikere),
]