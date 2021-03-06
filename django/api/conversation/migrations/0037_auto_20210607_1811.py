# Generated by Django 3.1.4 on 2021-06-07 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0036_auto_20210607_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applications',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Активный'),
        ),
        migrations.AlterField(
            model_name='applications',
            name='describe',
            field=models.TextField(default='', verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='applications',
            name='location',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.RESTRICT, related_name='us_loc', to='conversation.location', verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='applications',
            name='status',
            field=models.IntegerField(choices=[(0, 'ожидается'), (1, 'в пути'), (2, 'выполнено'), (3, 'отклонено')], default=1, verbose_name='статус'),
        ),
        migrations.AlterField(
            model_name='applications',
            name='title',
            field=models.CharField(default='', max_length=100, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='applications',
            name='typeOf',
            field=models.ManyToManyField(to='conversation.Typeof', verbose_name='Типы груов'),
        ),
        migrations.AlterField(
            model_name='applications',
            name='weight',
            field=models.CharField(max_length=50, verbose_name='Вес (кг)'),
        ),
    ]
