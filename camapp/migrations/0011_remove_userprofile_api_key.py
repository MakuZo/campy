# Generated by Django 2.1.1 on 2018-09-15 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camapp', '0010_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='api_key',
        ),
    ]
