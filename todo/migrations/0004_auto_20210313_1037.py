# Generated by Django 3.1.7 on 2021-03-13 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_todo_finished'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='finished',
            new_name='checked',
        ),
    ]
