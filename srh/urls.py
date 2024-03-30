from django.urls import path
from srh.views import *
app_name='any'

urlpatterns=[
    path('mayank/',mayank,name='mayank')
]