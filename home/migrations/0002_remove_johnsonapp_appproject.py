# Generated by Django 2.1.3 on 2019-01-26 05:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='johnsonapp',
            name='appProject',
        ),
    ]