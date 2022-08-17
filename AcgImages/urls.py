from django.urls import path,include
from rest_framework import routers
from AcgImages import views as AcgImagesView

router = routers.DefaultRouter()
router.register(r'upload', AcgImagesView.ImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('get',AcgImagesView.ShowImage.as_view()),
]