# Generated by Django 3.1.7 on 2021-03-19 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0017_auto_20210318_2107'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='item_type',
            field=models.CharField(default='Note', max_length=16),
        ),
    ]
