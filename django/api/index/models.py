from django.db import models
from django.contrib.auth.admin import User
from ckeditor.fields import RichTextField
from conversation.models import Location
from django.contrib.auth.models import AbstractUser


class UserData(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='moreData', verbose_name='Пользователь')
    location = models.ForeignKey(Location, on_delete=models.RESTRICT,
                                 related_name='user_location', blank=True, null=True, default=0, verbose_name='Адрес')
    number = models.CharField(
        max_length=100, blank=False, verbose_name='номер телефона')
    passportId = models.CharField(max_length=100, blank=True,
                                  verbose_name='Номер пасспорта')
    vk = models.CharField(max_length=100, blank=True,
                          verbose_name='токен авторизации vk')
    google = models.CharField(
        max_length=100, blank=True, verbose_name='токен авторизации google')
    appleId = models.CharField(
        max_length=100, blank=True, verbose_name='токен авторизации appleId')
    facebook = models.CharField(
        max_length=100, blank=True, verbose_name='токен авторизации facebook')
    avatar = models.ImageField(
        upload_to='static', blank=True, default='', verbose_name='фото')
    allowPush = models.BooleanField(
        default=True, verbose_name='разрешить уыедомления')
    blocked = models.BooleanField(default=False, verbose_name='заблокирован')

    def __str__(self):
        return f"{self.user}"

    class Meta:
        verbose_name = 'Дополнительное поле для пользователя'
        verbose_name_plural = 'Дополнительные поля для пользователя'


class Push(models.Model):
    title = models.CharField(
        max_length=50, verbose_name='Оглавление уведомления')
    describe = models.TextField(default='', verbose_name='Описание')
    photo = models.ImageField(
        upload_to='static', default='', verbose_name='Фото')
    slug = models.CharField(
        max_length=50, verbose_name='Для чего это уведомление')
    time = models.CharField(
        max_length=50, default='* * * * *', verbose_name='Время отправки пуша ()')

    def __str__(self):
        return f"{self.slug}"

    class Meta:
        verbose_name = 'Пуш уведомление'
        verbose_name_plural = 'Пуш уведомления'


class Support(models.Model):
    email = models.CharField(max_length=100, default='', verbose_name='Почта')
    title = models.CharField(max_length=100, default='',
                             verbose_name='Оглавление запроса')
    describe = models.TextField(default='', verbose_name='Описание проблемы')
    active = models.BooleanField(default=False, verbose_name='Просмотрено')

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = 'Вопрос обратной связи'
        verbose_name_plural = 'Вопрос обратной связи'


class General(models.Model):
    title = models.CharField(max_length=100, verbose_name='Главная')
    email = models.CharField(max_length=100, verbose_name='Почта')
    describe = RichTextField(default='', verbose_name='Описание')
    PlayMarket = models.TextField(
        default='', verbose_name='Ссылка на приложение в плей маркете')
    AppStore = models.TextField(
        default='', verbose_name='Ссылка на приложение в апп сторе')

    class Meta:
        verbose_name = 'Конфигурация приложение'
        verbose_name_plural = 'Конфигурация приложения'
