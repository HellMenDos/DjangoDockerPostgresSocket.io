from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.admin import User
from conversation.models import Location


class Info(models.Model):
    title = models.CharField(
        max_length=100, blank=True, verbose_name='Название')
    describe = RichTextField(default='', verbose_name='Описание')
    date = models.DateTimeField(verbose_name='Время', null=True, auto_now=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Информация'
        verbose_name_plural = 'Информация'


class Questions(models.Model):
    title = models.CharField(max_length=100, blank=True, verbose_name='Вопрос')
    describe = RichTextField(default='', verbose_name='Ответ')
    date = models.DateTimeField(verbose_name='Время', null=True, auto_now=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Вопросы для часто задаваемых вопросов'
        verbose_name_plural = 'Вопросы для часто задаваемых вопросов'


class Invation(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.RESTRICT, related_name='userFrom', verbose_name='Пользователь')
    hashurl = models.CharField(
        max_length=100, default='', verbose_name='Хэш для url')
    count = models.IntegerField(
        default=0, verbose_name='Количество приглашшенных пользователей')

    def __str__(self):
        return f"{self.user}"

    class Meta:
        verbose_name = 'Приглашение'
        verbose_name_plural = 'Приглашения'


class BonusGeneral(models.Model):
    level = models.IntegerField(default=0, verbose_name='Уровень')
    title = models.CharField(max_length=100, default='',
                             verbose_name='Оглавление бонусного уровня')
    describe = models.TextField(
        default='', verbose_name='Описание бонусного уровня')
    points = models.TextField(default='', verbose_name='Сколько очков')
    forUser = models.BooleanField(
        default=False, verbose_name='Для пользователя')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Уровень бонуса'
        verbose_name_plural = 'Уровни бонусов'


class Bonus(models.Model):
    level = models.ForeignKey(BonusGeneral, on_delete=models.RESTRICT,
                              related_name='bonusgeneral', default='', verbose_name='выбор уровня бонуса')
    location = models.ForeignKey(Location, on_delete=models.RESTRICT,
                                 related_name='location', default='', verbose_name='Место бонуса')
    title = models.CharField(max_length=100, default='',
                             verbose_name='Оглавление бонуса')
    describe = models.TextField(default='', verbose_name='Описание бонусна')
    points = models.CharField(
        max_length=100, default='', verbose_name='Вознограждение')
    forUser = models.BooleanField(
        default=False, verbose_name='Для пользователя')

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = 'Бонус'
        verbose_name_plural = 'Бонусы'


class RelationBonus(models.Model):
    bonus = models.ForeignKey(Bonus, on_delete=models.RESTRICT,
                              related_name='bonus', default='', verbose_name='Бонус')
    user = models.ForeignKey(User, on_delete=models.RESTRICT,
                             related_name='location', default='', verbose_name='Пользователь')

    def __str__(self):
        return f"{self.user}"

    class Meta:
        verbose_name = 'Связь пользователя с бонусами'
        verbose_name_plural = 'Связь пользователей с бонусами'
