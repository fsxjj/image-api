from django.db import models
from django.core.validators import RegexValidator

class WallPaintingOrder(models.Model):
    DIMENSION_CHOICES = [
        (1, '1'),
        (1.5, '1.5'),
        (2, '2'),
        (2.5, '2.5'),
        (3, '3'),
    ]

    name = models.CharField(max_length=100)
    phone_number = models.CharField(
        max_length=15,
        validators=[RegexValidator(r'^\+?\d{10,15}$', message="Enter a valid phone number.")]
    )
    location = models.CharField(max_length=255)
    length = models.FloatField(choices=DIMENSION_CHOICES)
    width = models.FloatField(choices=DIMENSION_CHOICES)
    colored = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.location}"
