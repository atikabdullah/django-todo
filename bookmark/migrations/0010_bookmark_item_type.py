# Generated by Django 3.1.7 on 2021-03-19 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0009_auto_20210318_2100'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='item_type',
            field=models.CharField(default='Bookmark', max_length=16),
        ),
    ]
