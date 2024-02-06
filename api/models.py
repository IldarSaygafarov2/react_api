from django.db import models

from django.urls import reverse


class Product(models.Model):
    RATING_CHOICES = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    ]

    title = models.CharField(verbose_name='Название', max_length=255)
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Фото', upload_to='products/images/')
    rating = models.IntegerField(verbose_name='Рейтинг', choices=RATING_CHOICES, default=0)
    price = models.DecimalField(verbose_name='Цена', max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

