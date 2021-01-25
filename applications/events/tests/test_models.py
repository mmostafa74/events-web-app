from django.test import TestCase, tag
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError

from applications.events.models import Event

User = get_user_model()


@tag("testeventmodel")
class TestEventModel(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            email="test@test.com", password="testpass123"
        )
        self.title = "Test Title"
        self.description = "Test Description"
        self.date = "2021-3-14"

    def test_create_event_successful(self):
        event = Event.objects.create(
            title=self.title,
            description=self.description,
            date=self.date,
            author=self.user,
        )

        self.assertEqual(event.title, self.title)
        self.assertEqual(event.description, self.description)
        self.assertEqual(event.date, self.date)
        self.assertEqual(event.author, self.user)

    def test_new_event_invalid_user(self):
        with self.assertRaises(IntegrityError):
            Event.objects.create(
                title=self.title,
                description=self.description,
                date=self.date,
                author=None,
            )

    def test_new_event_invalid_date(self):
        with self.assertRaises(IntegrityError):
            Event.objects.create(
                title=self.title,
                description=self.description,
                date=None,
                author=self.user,
            )
