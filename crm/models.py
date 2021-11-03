from django.contrib.auth.models import User
from django.db import models


def customer_image_path(instance, filename):
    return f"media/uploads/{instance.first_name}/{filename}"


# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    created_by = models.ForeignKey(
        User, related_name="created", on_delete=models.CASCADE
    )
    updated_by = models.ForeignKey(
        User, related_name="updated", on_delete=models.CASCADE
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to=customer_image_path, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
