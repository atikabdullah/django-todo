# Generated by Django 3.1.7 on 2021-03-16 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0009_auto_20210316_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='tags',
            field=models.ManyToManyField(null=True, related_name='tagss', to='note.Tag'),
        ),
    ]
