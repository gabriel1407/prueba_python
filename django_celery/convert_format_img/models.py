from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ImagesFormat(models.Model):
    name = models.TextField()
    user = models.ForeignKey(User,on_delete=models.PROTECT)
    type_image = models.TextField()
    img = models.ImageField(upload_to='./public/img/', null=True)
    is_enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'con_Images_t'
    