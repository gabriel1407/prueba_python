from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Images(models.Model):
    name = models.TextField()
    user = models.ForeignKey(User,on_delete=models.PROTECT)
    type_image = models.TextField()
    is_enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'con_Images_t',
        app_label = 'convert_format_img'
    