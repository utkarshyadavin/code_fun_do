# Generated by Django 2.0.1 on 2018-02-02 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20180202_2103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='city',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name',
        ),
    ]
