from django.contrib.auth import get_user_model
from django.test import TestCase
from django.test.utils import tag
from django.urls import reverse, resolve

from applications.users.forms import CustomUserCreationForm
from applications.users.views import register


User = get_user_model()


@tag("testregisterview")
class TestRegisterView(TestCase):
    def setUp(self) -> None:
        url = reverse("users:register")
        self.response = self.client.get(url)
        self.email = "test@test.com"
        self.password = "testpass123"

    def test_register_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "users/register.html")
        self.assertContains(self.response, "Create an account")
        self.assertNotContains(self.response, "Hi there! I should not be on the page.")

    def test_register_form(self):
        form = self.response.context.get("form")
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, "csrfmiddlewaretoken")

    def test_register_view(self):
        view = resolve("/users/register/")
        self.assertEqual(view.func, register)
