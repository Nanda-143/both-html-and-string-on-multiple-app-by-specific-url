from django.urls import path
from app3.views import *
urlpatterns=[
    path('five/',five,name='five'),
    path('six/',six,name='six'),
    path('nothing/',nothing,name='nothing'),
]