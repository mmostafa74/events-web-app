from django.test import TestCase, tag
from django.contrib.auth import get_user_model

User = get_user_model()


@tag("usermodel")
class TestUserModel(TestCase):
    def test_create_user_successful(self):
        email = "test@test.com"
        password = "TestPass123"
        user = User.objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email = "test@TEST.com"
        password = "TestPass123"
        user = User.objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            User.objects.create_user(None, "testpass123")

    def test_create_super_user(self):
        user = User.objects.create_superuser("test@test.com", "TestPass123")

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
