# Generated by Django 3.1.4 on 2021-05-07 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0012_auto_20210507_1343'),
    ]

    operations = [
        migrations.CreateModel(
            name='Support',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Оглавление уведомления')),
                ('describe', models.TextField(default='', verbose_name='Описание')),
                ('photo', models.ImageField(default='', upload_to='static', verbose_name='Фото')),
                ('slug', models.CharField(max_length=30, verbose_name='Для чего это уведомление')),
            ],
            options={
                'verbose_name': 'Пуш уведомление',
                'verbose_name_plural': 'Пуш уведомления',
            },
        ),
    ]