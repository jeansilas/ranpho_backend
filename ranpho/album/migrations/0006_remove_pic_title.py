# Generated by Django 3.2.8 on 2021-11-05 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0005_auto_20211104_1726'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pic',
            name='title',
        ),
    ]
