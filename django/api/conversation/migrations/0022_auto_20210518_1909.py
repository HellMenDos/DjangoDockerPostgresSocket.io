# Generated by Django 3.1.4 on 2021-05-18 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0021_auto_20210518_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applications',
            name='location',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.RESTRICT, related_name='us_loc', to='conversation.location', verbose_name='Адрес'),
        ),
    ]
