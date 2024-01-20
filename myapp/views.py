from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import StoreModelSerializer
from .models import StoreModel



class StoreAPIVIEW(APIView):
  serializer_class = StoreModelSerializer
  parser_classes = (MultiPartParser, FormParser, JSONParser)
  
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
    
    
  def get(self,request):
    try:
       all = StoreModel.objects.all()
       serializer= self.serializer_class(instance=all, many=True)
       return Response(data=serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
      return Response(data={"error":e}, status=status.HTTP_400_BAD_REQUEST)
    
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
    
      
    