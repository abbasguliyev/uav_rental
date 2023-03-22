from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.urls import reverse
from apps.uav.models import Uav
from apps.order.models import Order

# Create your tests here.
class OrderTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(email='test@example.com', password='test')
        self.user.save()
        self.uav = Uav.objects.create(
            name="test", description="test", weight=10,
            endurance=10, flight_range=10, max_speed=100,
            price=1500
        )
        self.uav.save()

        self.order = Order.objects.create(user=self.user, uav=self.uav)
        self.order.save()

    def tearDown(self):
        self.order.delete()
        self.user.delete()
        self.uav.delete()

    def test_create_order(self):
        self.assertEqual(self.order.user, self.user)
        self.assertEqual(self.order.uav, self.uav)

class OderListViewTest(TestCase):
    def test_correct(self):
        url = reverse("order")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)


class OrderAddViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(email='test@example.com', password='test')
        self.user.save()
        self.uav = Uav.objects.create(
            name="test", description="test", weight=10,
            endurance=10, flight_range=10, max_speed=100,
            price=1500
        )
        self.uav.save()

        self.order = Order.objects.create(user=self.user, uav=self.uav)
        self.order.save()

    def tearDown(self):
        self.order.delete()
        self.user.delete()
        self.uav.delete()

    def test_correct(self):
        url = reverse("order_add")
        response = self.client.post(url, {'user':self.user, 'uav':self.uav})
        self.assertEqual(response.status_code, 302)
