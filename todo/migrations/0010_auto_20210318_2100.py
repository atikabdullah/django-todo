# Generated by Django 3.1.7 on 2021-03-18 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
        ('todo', '0009_auto_20210318_2058'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.AlterField(
            model_name='todo',
            name='tags',
            field=models.ManyToManyField(related_name='todo_tags', to='tags.Tag'),
        ),
    ]
