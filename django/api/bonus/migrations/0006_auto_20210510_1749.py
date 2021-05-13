# Generated by Django 3.1.4 on 2021-05-10 17:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bonus', '0005_auto_20210510_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invation',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, related_name='userFrom', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
