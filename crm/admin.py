from django.contrib import admin
from .models import Customer

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "created",
        "created_by",
        "updated",
        "updated_by",
        "photo",
    )
    list_filter = ("first_name", "last_name", "created", "updated")
