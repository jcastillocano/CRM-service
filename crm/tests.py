# Django
from django.test import TestCase

# Python
import json

# Django Rest Framework
from rest_framework.test import APIClient
from rest_framework import status

# Models
from crm.models import Customer
from django.contrib.auth.models import User


class CustomerTestCase(TestCase):
    def setUp(self):
        user = User(
            email="testing_login@crm.com",
            first_name="Testing",
            last_name="Testing",
            username="testing_login",
            is_staff=True,
        )
        user.set_password("admin123")
        user.save()
        self.user = user
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_create_customer_permission_denied(self):
        client = APIClient()
        test_customer = {
            "first_name": "test_user_from_unit_test",
            "last_name": "test_user_from_unit_test",
        }

        response = client.post("/v1/customer/", test_customer, format="json")

        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_customer(self):
        test_customer = {
            "first_name": "test_user_from_unit_test",
            "last_name": "test_user_from_unit_test",
        }

        response = self.client.post("/v1/customer/", test_customer, format="json")

        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("id", result)
        self.assertIn("first_name", result)
        self.assertIn("last_name", result)
        self.assertIn("photo", result)
        self.assertEqual(result["first_name"], test_customer["first_name"])
        self.assertEqual(result["last_name"], test_customer["last_name"])

    def test_update_customer(self):
        customer = Customer.objects.create(
            first_name="test_user",
            last_name="test_user",
            created_by=self.user,
            updated_by=self.user,
        )

        test_customer_update = {
            "first_name": "test_user_first_name",
            "last_name": "test_user_last_name",
        }

        response = self.client.put(
            f"/v1/customer/{customer.id}/", test_customer_update, format="json"
        )

        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result["first_name"], test_customer_update["first_name"])
        self.assertEqual(result["last_name"], test_customer_update["last_name"])

    def test_delete_customer(self):
        customer = Customer.objects.create(
            first_name="test_user",
            last_name="test_user",
            created_by=self.user,
            updated_by=self.user,
        )

        response = self.client.delete(f"/v1/customer/{customer.id}/", format="json")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        customer_exists = Customer.objects.filter(id=customer.id)
        self.assertFalse(customer_exists)

    def test_get_customer(self):
        Customer.objects.create(
            first_name="test_user",
            last_name="test_user",
            created_by=self.user,
            updated_by=self.user,
        )

        Customer.objects.create(
            first_name="test_user_2",
            last_name="test_user_2",
            created_by=self.user,
            updated_by=self.user,
        )

        response = self.client.get("/v1/customer/")

        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(result), 2)
        for customer in result:
            self.assertIn("id", customer)
            self.assertIn("first_name", customer)
            self.assertIn("last_name", customer)
            self.assertIn("photo", customer)


class UserTestCase(TestCase):
    def setUp(self):
        self.basic_user = User(
            email="basic@crm.com",
            first_name="Basic",
            last_name="User",
            username="basic_user",
            is_staff=True,
            is_superuser=False,
        )
        self.basic_user.set_password("basic_password")
        self.basic_user.save()

    def test_get_users_permission_denied(self):
        client = APIClient()
        client.force_authenticate(user=self.basic_user)

        response = self.client.get("/v1/user/")

        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
