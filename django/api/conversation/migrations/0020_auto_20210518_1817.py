# Generated by Django 3.1.4 on 2021-05-18 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0022_auto_20210516_1023'),
        ('conversation', '0019_auto_20210516_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='company',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.RESTRICT, related_name='user_proposal', to='index.userdata', verbose_name='выбор пользователя'),
        ),
    ]
