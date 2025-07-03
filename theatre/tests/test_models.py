import pytest
from theatre.models import User, Actor, Genre, Play, TheatreHall, Performance

@pytest.mark.django_db
def test_create_user():
    user = User.objects.create_user(email="test@example.com", password="pass")
    assert user.email == "test@example.com"
    assert user.check_password("pass")

@pytest.mark.django_db
def test_create_actor_genre_play():
    actor = Actor.objects.create(first_name="Tom", last_name="Hanks")
    genre = Genre.objects.create(name="Drama")
    play = Play.objects.create(title="Hamlet", description="Classic tragedy")
    play.actors.add(actor)
    play.genres.add(genre)
    assert play.actors.count() == 1
    assert play.genres.count() == 1

@pytest.mark.django_db
def test_theatre_hall_and_performance():
    hall = TheatreHall.objects.create(name="Big Hall", rows=10, seats_in_row=10)
    play = Play.objects.create(title="Test Play", description="...")
    perf = Performance.objects.create(play=play, theatre_hall=hall, show_time="2030-01-01T18:00:00Z")
    assert perf.theatre_hall.name == "Big Hall"
