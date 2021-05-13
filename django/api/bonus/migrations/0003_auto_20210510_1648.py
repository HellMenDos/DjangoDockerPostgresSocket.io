# Generated by Django 3.1.4 on 2021-05-10 16:48

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bonus', '0002_auto_20210507_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='describe',
            field=ckeditor.fields.RichTextField(default='', verbose_name='Ответ'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='title',
            field=models.CharField(blank=True, max_length=30, verbose_name='Вопрос'),
        ),
        migrations.CreateModel(
            name='Invation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hashurl', models.CharField(default='', max_length=30, verbose_name='Хэш для url')),
                ('count', models.IntegerField(verbose_name='Количество приглашшенных пользователей')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='userFrom', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Приглашение',
                'verbose_name_plural': 'Приглашения',
            },
        ),
    ]