from .models import images
from .serializers import FileSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from picgo_backend import settings
from rest_framework.response import Response
import random
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__)) #项目目录
sys.path.append(BASE_DIR)
import GlobalValue
# Create your views here.

class ImageViewSet(viewsets.ModelViewSet):
    queryset = images.objects.all()
    serializer_class = FileSerializer

class ShowImage(APIView):
    def get(self,request):
        image_list = images.objects.all()
        n = len(image_list)
        image_ret = GlobalValue.BACKEND_URL + image_list[random.randint(0,n-1)].img.url
        return Response({
                'status': True,
                'data': image_ret,
            })