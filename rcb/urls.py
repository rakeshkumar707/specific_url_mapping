from django.urls import path
from rcb.views import *
app_name='abcd'

urlpatterns=[
    path('virat/',virat,name='virat')
]