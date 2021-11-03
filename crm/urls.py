from django.urls import include, path
from rest_framework import routers
from .views import CustomerViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r"customer", CustomerViewSet)
router.register(r"user", UserViewSet)

urlpatterns = [path("", include(router.urls))]
