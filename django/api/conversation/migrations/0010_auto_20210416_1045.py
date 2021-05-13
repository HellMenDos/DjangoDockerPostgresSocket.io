# Generated by Django 3.1.4 on 2021-04-16 10:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('conversation', '0009_auto_20210416_1021'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='room',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.RESTRICT, related_name='communicate', to='conversation.commucate', verbose_name='выбор комнаты'),
        ),
        migrations.AlterField(
            model_name='commucate',
            name='userFrom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='from_messages', to=settings.AUTH_USER_MODEL, verbose_name='Сообщение от'),
        ),
        migrations.AlterField(
            model_name='commucate',
            name='userTo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='to_messages', to=settings.AUTH_USER_MODEL, verbose_name='Сообщение для'),
        ),
        migrations.AlterField(
            model_name='review',
            name='userFrom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='from_reviews', to=settings.AUTH_USER_MODEL, verbose_name='Отзыв от'),
        ),
        migrations.AlterField(
            model_name='review',
            name='userTo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='to_reviews', to=settings.AUTH_USER_MODEL, verbose_name='Отзыв для'),
        ),
    ]