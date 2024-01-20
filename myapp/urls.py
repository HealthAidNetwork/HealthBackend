
from django.urls import path, include
from .views import storeAPI

urlpatterns = [

    path('store',  storeAPI)
]
