from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.admin import User


class Info(models.Model):
    title = models.CharField(max_length=30,blank=True, verbose_name='Название')
    describe = RichTextField(default='',verbose_name='Описание')
    date = models.DateTimeField(verbose_name='Время',null=True,auto_now=True)   

    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name = 'Информация'
        verbose_name_plural = 'Информация'

class Questions(models.Model):
    title = models.CharField(max_length=30,blank=True, verbose_name='Вопрос')
    describe = RichTextField(default='',verbose_name='Ответ')
    date = models.DateTimeField(verbose_name='Время',null=True,auto_now=True)   

    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name = 'Вопросы для часто задаваемых вопросов'
        verbose_name_plural = 'Вопросы для часто задаваемых вопросов'

class Invation(models.Model):
    user = models.OneToOneField(User,on_delete=models.RESTRICT,related_name='userFrom',verbose_name='Пользователь')
    hashurl = models.CharField(max_length=30,default='',verbose_name='Хэш для url')
    count = models.IntegerField(default=0,verbose_name='Количество приглашшенных пользователей') 

    def __str__(self):
        return f"{self.user}"
    
    class Meta:
        verbose_name = 'Приглашение'
        verbose_name_plural = 'Приглашения'