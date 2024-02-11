from django.db import models
from django.core.validators import MaxValueValidator
from django.urls import reverse


class Product(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255)
    description = models.TextField(verbose_name='Описание')
    image = models.URLField(verbose_name='Фото', null=True)
    rating = models.FloatField(verbose_name='Рейтинг', default=0, validators=[MaxValueValidator(5)])
    price = models.DecimalField(verbose_name='Цена', max_digits=6, decimal_places=2)
    quantity = models.IntegerField(verbose_name='Кол-во', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
