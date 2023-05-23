# Generated by Django 3.2.8 on 2021-11-06 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities_board', '0002_auto_20211106_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='category',
            field=models.ManyToManyField(to='activities_board.Category'),
        ),
        migrations.AlterField(
            model_name='event',
            name='type',
            field=models.BooleanField(default=False, verbose_name='Онлайн'),
        ),
    ]
