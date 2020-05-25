from django.db import models

# Create your models here.


class Order(models.Model):
    STATUS_CHOICES = (
        ('Completed', 'Completed'),
        ('Accepted', 'Accepted'),
        ('Running', 'Running'),
        ('Canceled', 'Canceled'),
    )

    # user = models.ForeignKey(User, related_name='bonuses', on_delete=models.CASCADE, null=True)
    location = models.CharField(max_length=100, verbose_name='Location', default="")
    date = models.DateField(verbose_name='Дата выполнения заказа', default="")
    start_of_walk = models.TimeField(auto_now=False, auto_now_add=False)
    end_of_walk = models.TimeField(auto_now=False, auto_now_add=False)
    created_at = models.DateTimeField(verbose_name='Дата создания заказа', auto_now_add=True)
    name = models.CharField(max_length=100, verbose_name='Name', default="")
    breed = models.CharField(max_length=100, verbose_name='Breed', default="")
    size = models.IntegerField('Size', default=0)
    price = models.DecimalField('Price', max_digits=7, decimal_places=2, default=0)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES,
                              default=STATUS_CHOICES[1][0], verbose_name='Статус заказа', null=True)
    additional_option = models.CharField(max_length=200, verbose_name='Дополнительные опции', default="", blank=True)
