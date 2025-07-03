import pytest
from rest_framework.test import APIClient
from theatre.models import User, Play, Performance, TheatreHall

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user():
    return User.objects.create_user(email="user@test.com", password="pass")

@pytest.fixture
def auth_client(api_client, user):
    response = api_client.post("/api/token/", {"email": user.email, "password": "pass"})
    token = response.data["token"]
    api_client.credentials(HTTP_AUTHORIZATION=f"Token {token}")
    return api_client

@pytest.mark.django_db
def test_get_plays(api_client):
    Play.objects.create(title="Romeo", description="Romance")
    response = api_client.get("/api/plays/")
    assert response.status_code == 200
    assert len(response.data) == 1

@pytest.mark.django_db
def test_create_reservation_with_tickets(auth_client):
    hall = TheatreHall.objects.create(name="Main", rows=5, seats_in_row=5)
    play = Play.objects.create(title="Show", description="...")
    perf = Performance.objects.create(play=play, theatre_hall=hall, show_time="2030-01-01T18:00:00Z")

    response = auth_client.post("/api/reservations/", {
        "tickets": [
            {"performance": perf.id, "row": 1, "seat": 1},
            {"performance": perf.id, "row": 1, "seat": 2}
        ]
    }, format="json")

    assert response.status_code == 201
