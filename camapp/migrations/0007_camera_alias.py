# Generated by Django 2.1.1 on 2018-09-10 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camapp', '0006_auto_20180910_2038'),
    ]

    operations = [
        migrations.AddField(
            model_name='camera',
            name='alias',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
