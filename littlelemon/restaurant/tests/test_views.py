from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from ..models import Menu
from ..serializers import MenuSerializer
from django.contrib.auth.models import User

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

        self.menu1 = Menu.objects.create(title="Spaghetti", price=150, inventory=20)
        self.menu2 = Menu.objects.create(title="Lasagna", price=180, inventory=15)
        self.menu3 = Menu.objects.create(title="Risotto", price=130, inventory=25)
        self.all_menus_url = reverse('menu-items-list')

    def test_getall(self):
        response = self.client.get(self.all_menus_url)
        
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
