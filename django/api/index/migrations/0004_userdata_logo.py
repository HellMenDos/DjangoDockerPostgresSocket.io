# Generated by Django 3.1.4 on 2021-04-14 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20210414_0914'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='logo',
            field=models.FileField(default='', upload_to='static'),
        ),
    ]
