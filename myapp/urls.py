
from django.urls import path, include
from .views import storeAPI, usersUploadAPI

urlpatterns = [
    path('store',  storeAPI),
    path('uploads',  usersUploadAPI),
    path('getuploads/<str:email>',  usersUploadAPI)
]
