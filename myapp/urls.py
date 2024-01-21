
from django.urls import path, include
from .views import storeAPI, usersUploadAPI

urlpatterns = [
    path('store',  storeAPI),
    path('uploads/<str:email>',  usersUploadAPI),
]
