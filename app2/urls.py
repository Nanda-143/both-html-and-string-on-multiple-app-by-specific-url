from django.urls import path
from app2.views import *
urlpatterns=[
    path('third/',third,name='third'),
    path('four/',four,name='four'),
    path('run/',run,name='run'),
]