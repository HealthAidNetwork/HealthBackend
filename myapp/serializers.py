from rest_framework import serializers
from .models import StoreModel, UsersUpload

class StoreModelSerializer(serializers.ModelSerializer):
  class Meta:
    model = StoreModel
    fields = "__all__"
    

class UsersUploadModelSerializer(serializers.ModelSerializer):
  class Meta:
    model = UsersUpload
    fields = "__all__"