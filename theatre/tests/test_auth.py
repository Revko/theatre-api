import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from theatre.models import User

@pytest.mark.django_db
def test_token_auth():
    client = APIClient()
    user = User.objects.create_user(email="user@test.com", password="pass1234")
    response = client.post(reverse("token_obtain"), {
        "email": "user@test.com",
        "password": "pass1234"
    })
    assert response.status_code == 200
    assert "token" in response.data
