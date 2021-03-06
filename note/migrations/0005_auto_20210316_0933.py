# Generated by Django 3.1.7 on 2021-03-16 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0004_auto_20210316_0930'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='card_description',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='description',
            field=models.TextField(max_length=8000, null=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
