from django.urls import path
from csk.views import *
aap_name='something'

urlpatterns=[
    path('rutu/',rutu,name='rutu'),
]