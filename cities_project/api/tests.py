from django.test import TestCase
from django.urls import reverse
from .models import Product, City, PhotoLink
from rest_framework.test import APITestCase
from rest_framework import status
from types import NoneType


class ProductModelTest(APITestCase):

    def setUp(self):
        self.product = Product.objects.create(name="Test Product")

    def test_product_creation(self):
        self.assertEqual(self.product.name, "Test Product")
        self.assertIsInstance(self.product, Product)
        self.assertEqual(Product.objects.count(), 1)


class CityModelTest(TestCase):

    def setUp(self):
        self.city = City.objects.create(name="Test City")

    def test_city_creation(self):
        self.assertEqual(self.city.name, "Test City")
        self.assertIsInstance(self.city, City)
        self.assertEqual(City.objects.count(), 1)


class PhotoLinkModelTest(TestCase):

    def setUp(self):
        self.product = Product.objects.create(name="Test Product")
        self.city = City.objects.create(name="Test City")
        self.all_cities_photo_link = PhotoLink.objects.create(
            product=self.product,
            photo_link="all_city_picture.jpg",
            city=None
        )
        self.private_city_photo_link = PhotoLink.objects.create(
            product=self.product,
            photo_link="city_specific_photo.jpg",
            city=self.city
        )

    def test_photo_link_creation(self):
        self.assertEqual(self.all_cities_photo_link.photo_link,
                         "all_city_picture.jpg")
        self.assertEqual(self.all_cities_photo_link.product, self.product)
        self.assertIsNone(self.all_cities_photo_link.city)
        self.assertIsInstance(self.all_cities_photo_link.city, NoneType)
        self.assertEqual(PhotoLink.objects.count(), 2)

        self.assertEqual(self.private_city_photo_link.photo_link,
                         "city_specific_photo.jpg")
        self.assertEqual(self.private_city_photo_link.product, self.product)
        self.assertEqual(self.private_city_photo_link.city, self.city)
        self.assertIsInstance(self.private_city_photo_link.city, City)
        self.assertEqual(PhotoLink.objects.count(), 2)


class ProductAPITestCase(APITestCase):

    def setUp(self):
        self.product = Product.objects.create(name="Test Product")

        self.city = City.objects.create(name="Test City")

        self.city_photo_link = PhotoLink.objects.create(
            product=self.product,
            photo_link="city_specific_photo.jpg",
            city=self.city
        )

        self.all_cities_photo_link = PhotoLink.objects.create(
            product=self.product,
            photo_link="all_cities_photo.jpg",
            city=None
        )

    def test_get_products_with_city_header(self):
        url = reverse('product_api')

        headers = {'HTTP_City': str(self.city.id)}

        response = self.client.get(url, **headers)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data[0]['photo_links']), 1)
        self.assertEqual(response.data[0]['photo_links'][0]['photo_link'], 'city_specific_photo.jpg')

    def test_get_products_without_city_header(self):
        url = reverse('product_api')

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data[0]['photo_links']), 1)
        self.assertEqual(response.data[0]['photo_links'][0]['photo_link'], 'all_cities_photo.jpg')
