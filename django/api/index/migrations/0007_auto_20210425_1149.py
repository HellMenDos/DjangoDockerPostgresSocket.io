# Generated by Django 3.1.4 on 2021-04-25 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_auto_20210416_0758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='avavtar',
            field=models.ImageField(default='', upload_to='static', verbose_name='фото'),
        ),
    ]
