# Generated by Django 3.1.4 on 2021-04-25 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_auto_20210425_1149'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdata',
            old_name='avavtar',
            new_name='avatar',
        ),
    ]