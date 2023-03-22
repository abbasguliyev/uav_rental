from django.test import TestCase
from django.urls import reverse
from apps.uav.models import Uav, Category, Brand

# Create your tests here.
class UavTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(category_name="test_category")
        self.category.save()
        self.brand = Brand.objects.create(brand_name="test_brand")
        self.brand.save()
        self.uav = Uav.objects.create(
            name="test", description="test", category=self.category, brand=self.brand, weight=10,
            endurance=10, flight_range=10, max_speed=100, price=1500
        )
        self.uav.save()

    def tearDown(self):
        self.uav.delete()
        self.category.delete()
        self.brand.delete()

    def test_create_uav(self):
        self.assertEqual(self.uav.name, "test")
        self.assertEqual(self.uav.description, "test")
        self.assertEqual(self.uav.category, self.category)
        self.assertEqual(self.uav.brand, self.brand)
        self.assertEqual(self.uav.weight, 10)
        self.assertEqual(self.uav.endurance, 10)
        self.assertEqual(self.uav.flight_range, 10)
        self.assertEqual(self.uav.max_speed, 100)
        self.assertEqual(self.uav.price, 1500)

class UavListViewTest(TestCase):
    def test_correct(self):
        url = reverse("home")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

class UavDashboardListViewTest(TestCase):
    def test_correct(self):
        url = reverse("uav_dashboard")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

class UavAddViewTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(category_name="test_category")
        self.category.save()
        self.brand = Brand.objects.create(brand_name="test_brand")
        self.brand.save()
        self.uav = Uav.objects.create(
            name="test", description="test", category=self.category, brand=self.brand, weight=10,
            endurance=10, flight_range=10, max_speed=100, price=1500
        )
        self.uav.save()

    def tearDown(self):
        self.uav.delete()
        self.category.delete()
        self.brand.delete()

    def test_correct(self):
        url = reverse("uav_add")
        response = self.client.post(url, {
            'name':"test", 'description':"test", 'category':self.category, 'brand':self.brand, 'weight':10,
            'endurance':10, 'flight_range':10, 'max_speed':100, 'price':1500
        })
        self.assertEqual(response.status_code, 302)

class CategoryTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(category_name="test_category")
        self.category.save()

    def tearDown(self):
        self.category.delete()

    def test_create_uav(self):
        self.assertEqual(self.category.category_name, "test_category")

class BrandTest(TestCase):
    def setUp(self):
        self.brand = Brand.objects.create(brand_name="test_brand")
        self.brand.save()

    def tearDown(self):
        self.brand.delete()

    def test_create_uav(self):
        self.assertEqual(self.brand.brand_name, "test_brand")

class CategoryListViewTest(TestCase):
    def test_correct(self):
        url = reverse("category")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

class BrandListViewTest(TestCase):
    def test_correct(self):
        url = reverse("brand")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)


class CategoryAddViewTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(category_name="test_category")
        self.category.save()

    def tearDown(self):
        self.category.delete()

    def test_correct(self):
        url = reverse("category_add")
        response = self.client.post(url, {'category_name':"test_category"})
        self.assertEqual(response.status_code, 302)

class BrandAddViewTest(TestCase):
    def setUp(self):
        self.brand = Brand.objects.create(brand_name="test_brand")
        self.brand.save()

    def tearDown(self):
        self.brand.delete()

    def test_correct(self):
        url = reverse("brand_add")
        response = self.client.post(url, {'brand_name':"test_brand"})
        self.assertEqual(response.status_code, 302)
