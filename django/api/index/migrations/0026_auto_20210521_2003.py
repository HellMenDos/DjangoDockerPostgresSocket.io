# Generated by Django 3.1.4 on 2021-05-21 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0025_auto_20210519_1317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='support',
            name='isAdmin',
        ),
        migrations.RemoveField(
            model_name='support',
            name='user',
        ),
        migrations.AddField(
            model_name='support',
            name='email',
            field=models.CharField(default=3, max_length=30, verbose_name='Почта'),
            preserve_default=False,
        ),
    ]
