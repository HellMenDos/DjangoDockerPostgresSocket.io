# Generated by Django 3.1.4 on 2021-05-07 16:16

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bonus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='describe',
            field=ckeditor.fields.RichTextField(default='', verbose_name='Описание'),
        ),
    ]
