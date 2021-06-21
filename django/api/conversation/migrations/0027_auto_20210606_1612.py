# Generated by Django 3.1.4 on 2021-06-06 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0026_auto_20210521_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applications',
            name='title',
            field=models.CharField(default='', max_length=100, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='typeof',
            name='color',
            field=models.CharField(default='', max_length=100, verbose_name='Цвет в формате HEX'),
        ),
        migrations.AlterField(
            model_name='typeof',
            name='title',
            field=models.CharField(default='', max_length=100, verbose_name='Название типа'),
        ),
    ]