# Generated by Django 3.0.6 on 2020-05-24 13:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images/')),
                ('list_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
