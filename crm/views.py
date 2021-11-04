from rest_framework import viewsets
from .serializers import CustomerSerializer, UserSerializer
from .models import Customer
from django.contrib.auth.models import User
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all().order_by("created")
    serializer_class = CustomerSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(created_by=user, updated_by=user)

    def perform_update(self, serializer):
        user = self.request.user
        serializer.save(updated_by=user)


class IsSuperUser(IsAdminUser):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("date_joined")
    serializer_class = UserSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated & IsSuperUser]
