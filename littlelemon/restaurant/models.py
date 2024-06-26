from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateField()

    def __str__(self):
      return f'{self.name} : {str(self.booking_date)}'


class Menu(models.Model):
   title = models.CharField(max_length=255) 
   price = models.DecimalField(decimal_places=2, max_digits=5) 
   inventory = models.IntegerField()

   def __str__(self):
      return f'{self.title} : {str(self.price)}'