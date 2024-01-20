from django.db import models

# Create your models here.


class StoreModel(models.Model):
  name = models.CharField(null=True, blank=True, max_length=100)
  expiration = models.DateField(null=True, blank=True, max_length=100)
  image1 = models.FileField(verbose_name="Image1",null=True,  blank=True, upload_to="images")
  image2 = models.FileField(verbose_name="Image2",null=True,  blank=True, upload_to="images")
  available = models.BooleanField(default=True, blank=True)
  quantity = models.PositiveIntegerField(default=0, blank=True)
  
  
  def __str__(self):
    return f"{self.name}"
  
  class Meta:
      ordering = ('-pk',)