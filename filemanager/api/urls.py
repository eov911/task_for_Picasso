#from .views import get_file, upload
from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import ApiViewSet, DownloadViewSet

router = SimpleRouter()
router.register('api/v1/files', ApiViewSet)
router.register('api/v1/upload', DownloadViewSet)

'''urlpatterns = [
    path('api/v1/api/get_file/<int:pk>', get_file),
    path('api/v1/api/upload', upload),
]'''
