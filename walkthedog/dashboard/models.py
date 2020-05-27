from django.db import models

# Create your models here.
from walkthedog.users.models import User


class Order(models.Model):
    STATUS_CHOICES = (
        ('Completed', 'Completed'),
        ('Accepted', 'Accepted'),
        ('Running', 'Running'),
        ('Canceled', 'Canceled'),
    )

    user = models.ForeignKey(User, related_name='users', on_delete=models.CASCADE)
    location = models.CharField(max_length=100, verbose_name='Location')
    date = models.DateField(verbose_name='Дата выполнения заказа')
    start_of_walk = models.CharField(max_length=10, verbose_name='start_of_walk ')
    end_of_walk = models.CharField(max_length=10, verbose_name='end_of_walk')
    created_at = models.DateTimeField(verbose_name='Дата создания заказа', auto_now_add=True)
    name = models.CharField(max_length=100, verbose_name='Name')
    breed = models.CharField(max_length=100, verbose_name='Breed')
    size = models.IntegerField('Size')
    price = models.DecimalField('Price', max_digits=7, decimal_places=2)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES,
                              default=STATUS_CHOICES[1][0], verbose_name='Статус заказа', null=True)
    additional_option = models.CharField(max_length=200, verbose_name='Дополнительные опции', default="", blank=True)
    coordinates = models.CharField(max_length=150, verbose_name="координаты", default="")
