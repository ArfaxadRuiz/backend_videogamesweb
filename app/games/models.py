from django.db import models
from django.conf import settings
# Create your models here.
class Game(models.Model):

    OWNED_CHOICES = [
        ('physical', 'Físico'),
        ('digital', 'Digital'),
        ('both', 'Físico y Digital'),
        ('wishlist', 'Deseado'),
    ]

    STATUS_CHOICES = [
        ('no-played', 'No jugado'),
        ('playing', 'Jugando'),
        ('finished', 'Terminado'),
    ]

    title = models.CharField(max_length=200)
    console = models.CharField(max_length=100)
    owned = models.CharField(max_length=20, choices=OWNED_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    image = models.ImageField(upload_to='games/', null=True, blank=True)

    user = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    related_name='games'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title