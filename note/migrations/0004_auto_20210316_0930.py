# Generated by Django 3.1.7 on 2021-03-16 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0003_auto_20210315_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='description',
            field=models.TextField(max_length=8000),
        ),
    ]
