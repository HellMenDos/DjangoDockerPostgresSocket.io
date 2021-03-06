# Generated by Django 3.1.4 on 2021-05-03 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0015_auto_20210501_1419'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='applications',
            options={'verbose_name': 'Заявка', 'verbose_name_plural': 'Заявки'},
        ),
        migrations.AlterModelOptions(
            name='commucate',
            options={'verbose_name': 'Комната', 'verbose_name_plural': 'Комнаты'},
        ),
        migrations.AlterModelOptions(
            name='location',
            options={'verbose_name': 'Адрес', 'verbose_name_plural': 'Адреса'},
        ),
        migrations.AlterModelOptions(
            name='messages',
            options={'verbose_name': 'Сообщение', 'verbose_name_plural': 'Сообщение'},
        ),
        migrations.AlterModelOptions(
            name='proposal',
            options={'verbose_name': 'Предложение для заявок', 'verbose_name_plural': 'Предложения для заявок'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
        migrations.AlterModelOptions(
            name='typeof',
            options={'verbose_name': 'Тип груза', 'verbose_name_plural': 'Типы грузов'},
        ),
        migrations.AddField(
            model_name='typeof',
            name='color',
            field=models.CharField(default='', max_length=30, verbose_name='Цвет в формате HEX'),
        ),
        migrations.AlterField(
            model_name='applications',
            name='typeOf',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='user_aplications', to='conversation.typeof', verbose_name='К какому типу принадлежит'),
        ),
    ]
