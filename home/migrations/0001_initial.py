# Generated by Django 2.1.3 on 2019-01-26 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JohnsonApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appTitle', models.CharField(max_length=200)),
                ('appProject', models.CharField(max_length=200)),
                ('appPathName', models.CharField(max_length=200)),
            ],
        ),
    ]
