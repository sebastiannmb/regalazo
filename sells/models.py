from django.db import models

# Create your models here.
class Sells(models.Model):
    CHOICES = (
        ('Cash', 'Cash'),
        ('Card', 'Card'),
    )

    seller = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    quantity = models.IntegerField()
    creation_time = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(choices=CHOICES, max_length=4)
