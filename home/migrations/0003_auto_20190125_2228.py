# Generated by Django 2.1.3 on 2019-01-26 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_johnsonapp_appproject'),
    ]

    operations = [
        migrations.RenameField(
            model_name='johnsonapp',
            old_name='appPathName',
            new_name='appNameSpace',
        ),
    ]