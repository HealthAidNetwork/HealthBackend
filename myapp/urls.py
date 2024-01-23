
from django.urls import path, include
from .views import storeAPI, usersUploadAPI, delivery

urlpatterns = [
    path('store',  storeAPI),
    path('uploads/<str:email>',  usersUploadAPI),
    path('delivery',  delivery),
]
