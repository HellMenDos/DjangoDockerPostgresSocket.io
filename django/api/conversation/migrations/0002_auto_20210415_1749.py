# Generated by Django 3.1.4 on 2021-04-15 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Typeof',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=30)),
                ('describe', models.TextField(default='')),
            ],
        ),
        migrations.AddField(
            model_name='applications',
            name='weight',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='applications',
            name='typeof',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.RESTRICT, to='conversation.typeof'),
        ),
    ]
