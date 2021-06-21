# Generated by Django 3.1.4 on 2021-06-06 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0027_auto_20210606_1612'),
        ('index', '0027_auto_20210521_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='general',
            name='email',
            field=models.CharField(max_length=100, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='general',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Главная'),
        ),
        migrations.AlterField(
            model_name='support',
            name='email',
            field=models.CharField(default='', max_length=100, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='support',
            name='title',
            field=models.CharField(default='', max_length=100, verbose_name='Оглавление запроса'),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='appleId',
            field=models.CharField(blank=True, max_length=100, verbose_name='токен авторизации appleId'),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='facebook',
            field=models.CharField(blank=True, max_length=100, verbose_name='токен авторизации facebook'),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='google',
            field=models.CharField(blank=True, max_length=100, verbose_name='токен авторизации google'),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='location',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.RESTRICT, related_name='user_location', to='conversation.location', verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='number',
            field=models.CharField(max_length=100, verbose_name='номер телефона'),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='vk',
            field=models.CharField(blank=True, max_length=100, verbose_name='токен авторизации vk'),
        ),
    ]
