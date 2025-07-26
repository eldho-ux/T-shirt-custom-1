from email.policy import default

from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='img/')


# C - Create TShirt model
class TShirt(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    COLOR_CHOICES = [
        ('red', 'Red'),
        ('blue', 'Blue'),
        ('black', 'Black'),
        ('white', 'White'),
        ('green', 'Green'),
    ]

    SIZE_CHOICES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),

    ]


    color = models.CharField(max_length=10, choices=COLOR_CHOICES)
    size = models.CharField(max_length=2, choices=SIZE_CHOICES)
    design_image = models.ImageField(upload_to='tshirt_designs/', blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=299.00)

    def __str__(self):
        return f"{self.name} ({self.color}, {self.size})"

    # temporary

    class LaunchNotification(models.Model):
        phone_number = models.CharField(max_length=15)
        created_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.phone_number



