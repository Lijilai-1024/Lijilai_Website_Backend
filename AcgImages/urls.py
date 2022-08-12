from django.urls import path,include,re_path
from rest_framework import routers
from AcgImages import views as AcgImagesView
from picgo_backend import settings

router = routers.DefaultRouter()
router.register(r'upload', AcgImagesView.ImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('get',AcgImagesView.ShowImage.as_view()),
]