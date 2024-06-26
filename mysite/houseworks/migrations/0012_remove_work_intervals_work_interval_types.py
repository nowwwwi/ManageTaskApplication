# Generated by Django 5.0.4 on 2024-05-12 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houseworks', '0011_remove_work_interval_types_work_intervals'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work',
            name='intervals',
        ),
        migrations.AddField(
            model_name='work',
            name='interval_types',
            field=models.ManyToManyField(blank=True, related_name='works', to='houseworks.intervaltype'),
        ),
    ]
