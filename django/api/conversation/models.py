from django.db import models
from django.contrib.auth.admin import User
from datetime import date

class Typeof(models.Model):
    title = models.CharField(max_length=30,default='',verbose_name='Название типа')
    describe = models.TextField(default='',verbose_name='Данные')
    color = models.CharField(max_length=30,default='',verbose_name='Цвет в формате HEX')
    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Тип груза'
        verbose_name_plural = 'Типы грузов'

class Location(models.Model):
    title = models.CharField(max_length=30,default='',verbose_name='Адрес')
    describe = models.TextField(default='',verbose_name='Данные')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'


class Applications(models.Model):
    
    STATUS_CHOICES = (
        (0, 'ожидается'),
        (1, 'в пути'),
        (2, 'выполнено'),
        (3, 'отклонено'),
    )

    user = models.ForeignKey(User,on_delete=models.RESTRICT,related_name='user_aplications',default='',verbose_name='выбор пользователя')
    company = models.ForeignKey(User,on_delete=models.RESTRICT,related_name='company_aplications',blank=True,null=True,verbose_name='выбор компании')
    location = models.CharField(max_length=30,default='',verbose_name='Адрес')
    active = models.BooleanField(default=True,verbose_name='Активный')
    status = models.IntegerField(default=1,verbose_name='статус', choices=STATUS_CHOICES)
    title = models.CharField(max_length=30,default='',verbose_name='Заголовок')
    describe = models.TextField(default='',verbose_name='описание')
    photo = models.ImageField(upload_to='static',default='',verbose_name='фото')
    date = models.DateTimeField(verbose_name='Дата',null=True)  
    weight = models.IntegerField(default=1,verbose_name='Вес (кг)')
    typeOf = models.ForeignKey(Typeof,on_delete=models.RESTRICT,related_name='user_aplications',blank=True,null=True,verbose_name='К какому типу принадлежит')
    
    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class Proposal(models.Model):
    application = models.ForeignKey(Applications,on_delete=models.RESTRICT,related_name='user_proposal',default='',verbose_name='выбор заявки')
    company = models.ForeignKey(User,on_delete=models.RESTRICT,related_name='user_proposal',default='',verbose_name='выбор пользователя')
    describe = models.TextField(default='',verbose_name='описание')

    def __str__(self):
        return f"{self.application}"

    class Meta:
        verbose_name = 'Предложение от компании для заявок'
        verbose_name_plural = 'Предложениятот компаний для заявок'


class Commucate(models.Model):
    userFrom = models.ForeignKey(User,on_delete=models.RESTRICT,related_name='from_messages',verbose_name='Сообщение от')
    userTo = models.ForeignKey(User,on_delete=models.RESTRICT,related_name='to_messages',verbose_name='Сообщение для')
    
    def __str__(self):
        return f"{self.id}"
    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'


class Messages(models.Model):
    room = models.ForeignKey(Commucate,on_delete=models.RESTRICT,related_name='communicate',default=2,verbose_name='выбор комнаты')
    user = models.ForeignKey(User,on_delete=models.RESTRICT,related_name='user',default=1,verbose_name='какой пользователь')
    message = models.TextField(verbose_name='тело письма')
    date = models.DateTimeField(verbose_name='время',null=True,auto_now=True)   

    def __str__(self):
        return f"комната {self.room} -- пользователь {self.user}"
    
    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщение'


    
class Review(models.Model):
    userFrom = models.ForeignKey(User,on_delete=models.RESTRICT,related_name='from_reviews',verbose_name='Отзыв от')
    userTo = models.ForeignKey(User,on_delete=models.RESTRICT,related_name='to_reviews',verbose_name='Отзыв для')
    raiting = models.IntegerField(verbose_name='Рейтинг')
    describe = models.TextField(verbose_name='Описание')
    date = models.DateTimeField(verbose_name='Время',null=True,auto_now=True)   

    def __str__(self):
        return f"{self.userFrom}"
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'