# Generated by Django 3.1.4 on 2021-04-14 15:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('index', '0004_userdata_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdata',
            name='logo',
        ),
        migrations.AlterField(
            model_name='userdata',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='moreData', to=settings.AUTH_USER_MODEL),
        ),
    ]
