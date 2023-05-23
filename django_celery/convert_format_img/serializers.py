from django.contrib.auth.models import User
from rest_framework import serializers
from urllib.parse import unquote

from convert_format_img.models import ImagesFormat


class convert_format_img_Serializer(serializers.ModelSerializer):
    class Meta:
        model = ImagesFormat
        fields = ('__all__')

