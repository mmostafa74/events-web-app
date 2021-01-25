from django.contrib.auth import get_user_model
from django.test import TestCase
from django.test.utils import tag
from django.urls import reverse, resolve

from applications.events.models import Event
from applications.events.forms import EventForm
from applications.events.views import add_event


User = get_user_model()


@tag("testeventviews")
class TestEventViews(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            email="test@test.com", password="testpass123"
        )
        self.event = Event.objects.create(
            title="Test Title",
            description="Test Description!",
            date="2020-3-24",
            author=self.user,
        )

    def test_add_event_template(self):
        response = self.client.get(reverse("events:add_event"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "events/add_event.html")
        self.assertContains(response, "Add Event")
        self.assertNotContains(response, "Hi there! I should not be on the page.")

    def test_add_event_form(self):
        response = self.client.get(reverse("events:add_event"))
        form = response.context.get("form")
        self.assertIsInstance(form, EventForm)
        self.assertContains(response, "csrfmiddlewaretoken")

    def test_add_event_view(self):
        view = resolve("/events/add_event/")
        self.assertEqual(view.func, add_event)

    def test_add_event_view_response(self):
        response = self.client.post(
            reverse("events:add_event"),
            {
                "title": "New title",
                "description": "New text",
                "date": "2020-4-2",
                "author": self.user,
            },
        )

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "New title")
        self.assertContains(response, "New text")

    def test_edit_event_view(self):
        response = self.client.post(
            reverse("events:edit_event", args=f"{str(self.event.slug)}"),
            {
                "title": "Updated title",
                "description": "Updated text",
            },
        )

        self.assertEqual(response.status_code, 302)

    def test_post_delete_view(self):

        response = self.client.get(
            reverse("events:delete_event", args=str(self.event.slug))
        )

        self.assertEqual(response.status_code, 200)
