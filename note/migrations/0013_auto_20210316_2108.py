# Generated by Django 3.1.7 on 2021-03-16 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0012_auto_20210316_2037'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='card_description',
            new_name='text_content',
        ),
    ]
