from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import StoreModelSerializer, UsersUploadModelSerializer, DeliveryRequestModelSerializer
from .models import StoreModel, UsersUpload
import requests
import base64



class StoreAPIVIEW(APIView):
  serializer_class = StoreModelSerializer
  parser_classes = (MultiPartParser, FormParser, JSONParser)
  
  #Create a store item
  def post(self,request):
    try:
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
          inst= serializer.save()
          res = cloudinaryUpload(serializer.data['image'])
          inst.image_url = res
          inst.save()
          return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    except Exception as e:
      return Response(data={"error":e}, status=status.HTTP_400_BAD_REQUEST)
    
  #Get all available store items  
  def get(self,request):
    try:
       all = StoreModel.objects.all()
       serializer= self.serializer_class(instance=all, many=True)
       return Response(data=serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
      return Response(data={"error":e}, status=status.HTTP_400_BAD_REQUEST)
  #Edit a store item  
  def put(self, request):
    serializer_class = StoreModelSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    try:
        data = request.data
        obj = StoreModel.objects.get(pk= data['id'])
        serializer = self.serializer_class(instance=obj, data=data)
        if serializer.is_valid():
          serializer.save()
          # imagePath = processed = processImage(serializer.data['image'])
          
          return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    except Exception as e:
      return Response(data={"error":e}, status=status.HTTP_400_BAD_REQUEST)
    
    
storeAPI = StoreAPIVIEW.as_view()
    
    
    

    
class UsersUploadAPIVIEW(APIView):
  serializer_class = UsersUploadModelSerializer
  parser_classes = (MultiPartParser, FormParser, JSONParser)
  
  #Allows a user to make an image uplaod and it is saved to the useruploads model
  def post(self,request, email):
    try:
        data = request.data
  
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
          serializer.save()
          processed = processImage(serializer.data['image'])
          return Response(data={"data":serializer.data, "processed_data": processed}, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    except Exception as e:
      return Response(data={"error":e}, status=status.HTTP_400_BAD_REQUEST)
    
   #Get all the uploads by a user 
  def get(self,request, email):
    try:
       all = UsersUpload.objects.filter(email=email)
       serializer= self.serializer_class(instance=all, many=True)
       return Response(data=serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
      return Response(data={"error":e}, status=status.HTTP_400_BAD_REQUEST)
          

usersUploadAPI = UsersUploadAPIVIEW.as_view()


class DeliveryRequestAPIVIEW(APIView):
  serializer_class = DeliveryRequestModelSerializer
  parser_classes = (MultiPartParser, FormParser, JSONParser)
  #Allows a users to queue delivery
  def post(self,request):
    data = request.data
    try:
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
           
          serializer.save()
          return Response(data={"data":serializer.data}, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    except Exception as e:
      print(e)
      return Response(data={"error":e}, status=status.HTTP_400_BAD_REQUEST)
    
delivery = DeliveryRequestAPIVIEW.as_view()











import requests
import base64
from requests.exceptions import RequestException

ip = "34.201.114.120"

def processImage(image_path):
    base64_image = ""
    try:
        with open(f".{image_path}", "rb") as image_file:
            base64_image = base64.b64encode(image_file.read()).decode('utf-8')
    except FileNotFoundError as e:
        print(f"File not found: {image_path}")
        return None

    try:
        print("Sending request")
        response = requests.post(
            f'http://{ip}:8001/process',
            json={
                "image": base64_image,
                "prompt": "Just give me the text on the image, nothing else. Give me your best guess if you cannot read fully."
            }
        )
        response.raise_for_status()  # Raises an HTTPError for bad responses
        message = response.json()["message"]
        print(message)
        return message
    except RequestException as e:
        print(f"Error in request: {e}")





import cloudinary
import cloudinary.uploader
cloudinary.config(
  cloud_name = 'db0v83nmr', 
  api_key = '438937393957913', 
  api_secret = 'PvXKNxI-NXnn4JXp1jdKBDlaIZU'
)
def cloudinaryUpload(filePath):
  try:
      res = cloudinary.uploader.upload(f".{filePath}")
      return res['url']
  except Exception as e:
    print(e, "Cloudinary Error")
    return None
  
  