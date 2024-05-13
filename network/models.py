from django.db import models

from users.models import NULLABLE


class NetworkUnit(models.Model):
    """ Модель, описывающая объект сети """

    TYPE_CHOICES = [
        ('FA', 'Завод'),
        ('RN', 'Розничная сеть'),
        ('IE', 'Индивидуальный предприниматель')
    ]

    LEVEL_CHOICES = [
        ('0', 'Нулевой уровень'),
        ('1', 'Первый уровень'),
        ('2', 'Второй уровень')
    ]

    name = models.CharField(max_length=500, verbose_name='Название')
    type = models.CharField(max_length=30, choices=TYPE_CHOICES, verbose_name='Тип звена сети')
    level = models.CharField(max_length=15, choices=LEVEL_CHOICES, verbose_name='Уровень в иерархии поставок')

    email = models.EmailField(max_length=254, verbose_name='email', **NULLABLE)
    country = models.CharField(max_length=100, verbose_name='Страна', **NULLABLE)
    city = models.CharField(max_length=100, verbose_name='Город', **NULLABLE)
    street = models.CharField(max_length=100, verbose_name='Улица', **NULLABLE)
    house_number = models.CharField(max_length=15, verbose_name='Номер дома', **NULLABLE)

    supplier = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='Cсылка на поставщика',
                                 **NULLABLE)
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                               verbose_name='Задолженность перед поставщиком', **NULLABLE)
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return f'{self.name} - {self.type}'

    class Meta:
        verbose_name = 'Объект сети'
        verbose_name_plural = 'Объекты сети'


class Product(models.Model):
    """ Модель, описывающая продукт """
    name = models.CharField(max_length=150, verbose_name='название')
    model = models.CharField(max_length=150, verbose_name='модель', **NULLABLE)
    release_date = models.DateField(verbose_name='дата выхода продукта на рынок', **NULLABLE)
    network_unit = models.ForeignKey('NetworkUnit', on_delete=models.CASCADE, verbose_name='Объект сети')

    def __str__(self):
        return f'{self.name}, {self.model}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
