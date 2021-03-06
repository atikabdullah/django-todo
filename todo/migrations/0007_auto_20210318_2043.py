# Generated by Django 3.1.7 on 2021-03-18 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_auto_20210315_1954'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=28)),
            ],
        ),
        migrations.AddField(
            model_name='todo',
            name='tags',
            field=models.ManyToManyField(related_name='tags', to='todo.Tag'),
        ),
    ]
