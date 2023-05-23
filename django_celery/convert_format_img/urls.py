from django.urls import path
from django.urls.conf import include
from . import views
from convert_format_img.views import ImagesFormatViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'img_format', ImagesFormatViewSet)

urlpatterns = [
    path('test/', views.my_view, name='test'),
    path('test2/', views.my_view2, name='test2')
]

urlpatterns += router.urls