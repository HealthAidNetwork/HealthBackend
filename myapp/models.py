from django.db import models
import os
from datetime import datetime

# Create your models here.

def get_media_path(instance, file):
    # class_name = "media" // when you want to create another folder in the media folder
    dt = datetime.now()
    filename =  f"{instance}_${dt}_${file}" #added instance and datetime to the filename
    # return os.path.join(class_name,  filename) // this add a new media folder under the current existing media folder
    return os.path.join(filename)


class StoreModel(models.Model):
  name = models.CharField(null=True, blank=True, max_length=100)
  expiration = models.DateField(null=True, blank=True, max_length=100)
  image = models.FileField(verbose_name="Image",null=True,  blank=True, upload_to="media")
  available = models.BooleanField(default=True, blank=True)
  quantity = models.PositiveIntegerField(default=0, blank=True)
  
  
  def __str__(self):
    return f"{self.name}"
  
  class Meta:
      ordering = ('-pk',)
      

class UsersUpload(models.Model):
  email = models.CharField(null=True, blank=True, max_length=100)
  image = models.FileField(null=True,  blank=True, upload_to=get_media_path)
  medication = models.ForeignKey(StoreModel, null=True,  blank=True, on_delete= models.CASCADE)
  
  
  
  def __str__(self):
    return f"{self.email}"
  
class DeliveryRequest(models.Model):
  email = models.CharField(null=True, blank=True, max_length=100)
  address = models.CharField(null=True, blank=True, max_length=100)
  data = models.TextField(null=True, blank=True)
  country = models.CharField(null=True, blank=True, max_length=100)
  phonenumber = models.CharField(null=True, blank=True, max_length=100)
  
  
  def __str__(self):
    return f"{self.email}"
  
  
  