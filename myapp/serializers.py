from rest_framework import serializers
from .models import StoreModel, UsersUpload, DeliveryRequest

class StoreModelSerializer(serializers.ModelSerializer):
  class Meta:
    model = StoreModel
    fields = "__all__"
    

class UsersUploadModelSerializer(serializers.ModelSerializer):
  class Meta:
    model = UsersUpload
    fields = "__all__"
    
class DeliveryRequestModelSerializer(serializers.ModelSerializer):
  class Meta:
    model = DeliveryRequest
    fields = "__all__"