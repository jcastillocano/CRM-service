from django.contrib.auth.models import User
from django.db import models

def customer_image_path(instance, filename):
    return f'uploads/{instance.id}/{filename}'

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    created_by = models.ForeignKey(User, related_name='created', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, related_name='updated', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to=customer_image_path, null=True,
            blank=True)
