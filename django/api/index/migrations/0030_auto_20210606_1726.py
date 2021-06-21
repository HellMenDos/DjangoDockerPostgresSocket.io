# Generated by Django 3.1.4 on 2021-06-06 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0027_auto_20210606_1612'),
        ('index', '0029_auto_20210606_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='location',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='user_location', to='conversation.location', verbose_name='Адрес'),
        ),
    ]
