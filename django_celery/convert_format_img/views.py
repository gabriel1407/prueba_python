import requests
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework import status, serializers

from convert_format_img.models import ImagesFormat
from convert_format_img.serializers import convert_format_img_Serializer
from .tasks import invert_image_colors, convert_image_to_black
# Create your views here.

class ImagesFormatViewSet(ModelViewSet):
    queryset = ImagesFormat.objects.all().order_by('id')
    serializer_class = convert_format_img_Serializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('user_id', 'id', )

    def create(self, request, *args, **kwargs):
        serializer = convert_format_img_Serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(convert_format_img_Serializer(instance=serializer.instance).data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        serializer = convert_format_img_Serializer(
            instance=instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(convert_format_img_Serializer(instance=serializer.instance).data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def my_view(request):
    # Get the path to the image file from the request
    image_path = ImagesFormat.objects.filter(id = 2)
    
    data = list(image_path.values('img'))

    # Call the Celery task asynchronously
    invert_image_colors.delay(data)

    # Return a response to the client
    return JsonResponse({'status': 'ok', 'data': data}, safe=False)

def my_view2(request):
    # Get the path to the image file from the request
    image_path = ImagesFormat.objects.filter(id = 2)
    
    data = list(image_path.values('img'))

    # Call the Celery task asynchronously
    convert_image_to_black.delay(data)

    # Return a response to the client
    return JsonResponse({'status': 'ok', 'data': data}, safe=False)
