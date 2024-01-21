from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import StoreModelSerializer, UsersUploadModelSerializer
from .models import StoreModel, UsersUpload



class StoreAPIVIEW(APIView):
  serializer_class = StoreModelSerializer
  parser_classes = (MultiPartParser, FormParser, JSONParser)
  
  #Create a store item
  def post(self,request):
    try:
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
          serializer.save()
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
          return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    except Exception as e:
      return Response(data={"error":e}, status=status.HTTP_400_BAD_REQUEST)
    
   #Get all the uploads by a user 
  def get(self,request, email):
    try:
       print(email)
       all = UsersUpload.objects.filter(email=email)
       serializer= self.serializer_class(instance=all, many=True)
       return Response(data=serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
      return Response(data={"error":e}, status=status.HTTP_400_BAD_REQUEST)
          

usersUploadAPI = UsersUploadAPIVIEW.as_view()
    