# from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.db import models
#
# from django.contrib.auth.models import AbstractBaseUser

NULLABLE = {'blank': True, 'null': True}


# class CustomUser(AbstractBaseUser):
#     # Ваши поля модели пользователя
#
#     def save(self, *args, **kwargs):
#         # Хешируем пароль, если он был изменен
#         if self.pk is None or self.password != self._original_password:
#             self.set_password(self.password)
#
#         super().save(*args, **kwargs)
#
#     def set_password(self, raw_password):
#         self.password = make_password(raw_password)
#         self._original_password = self.password


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Email')
    first_name = models.CharField(max_length=20, verbose_name='Имя', **NULLABLE)
    last_name = models.CharField(max_length=30, verbose_name='Фамилия', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    verbose_name = 'пользователь'
    verbose_name_plural = 'пользователи'
