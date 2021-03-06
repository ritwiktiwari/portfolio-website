# Generated by Django 3.0.6 on 2020-05-23 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='summary',
            new_name='title',
        ),
        migrations.AddField(
            model_name='job',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='job',
            name='git_url',
            field=models.URLField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='job',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='job',
            name='project_url',
            field=models.URLField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='job',
            name='project_year',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
