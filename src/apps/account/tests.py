from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.urls import reverse

# Create your tests here.
class UserTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(email='test@example.com', password='test')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_create_user(self):
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertEqual(self.user.password, 'test')

    def test_update_user(self):
        self.user.email = "new_test@example.com"
        self.assertEqual(self.user.email, "new_test@example.com")

class RegisterViewTest(TestCase):
    def test_correct(self):
        url = reverse("register")
        response = self.client.post(url, {
            'first_name': 'Test', 'last_name': 'Test', 'email': 'test_example.com',
            'phone': '12345', 'address': 'test', 'company': 'test', 'password1': 'test123',
            'password2': 'test123'
        })
        self.assertEqual(response.status_code, 200)


class LoginViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(email='test@example.com', password='test')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        url = reverse("login")
        response = self.client.post(url, {'email':'test@example.com', 'password':'test'})
        self.assertEqual(response.status_code, 200)


class UserViewTest(TestCase):
    def test_correct(self):
        url = reverse("user")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
