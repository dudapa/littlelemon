from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Menu


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu1 = Menu.objects.create(title='aaa', price=1.00, inventory=1)
        self.menu2 = Menu.objects.create(title='bbb', price=2.00, inventory=2)
        self.menu3 = Menu.objects.create(title='ccc', price=3.00, inventory=3)
        self.url = '/api/menu-items/'

    def test_getall(self):
        response = self.client.get(self.url)
        response_data = [dict(item) for item in response.data]
        
        expected_data = [
            {'id' : self.menu1.id, 'title' : 'aaa', 'price' : '1.00', 'inventory' : 1},
            {'id' : self.menu2.id, 'title' : 'bbb', 'price' : '2.00', 'inventory' : 2},
            {'id' : self.menu3.id, 'title' : 'ccc', 'price' : '3.00', 'inventory' : 3}
        ]
    
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data, expected_data)