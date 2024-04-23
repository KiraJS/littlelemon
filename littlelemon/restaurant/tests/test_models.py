from django.test import TestCase
from ..models import Menu, Booking

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")

class BookingTest(TestCase):
    def test_get_item(self):
        item = Booking.objects.create(name="Bob", no_of_guests=2, booking_date="2024-12-02")
        self.assertEqual(str(item), "Bob : 2024-12-02")