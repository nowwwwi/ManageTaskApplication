# Generated by Django 5.0.4 on 2024-05-05 00:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('houseworks', '0002_alter_work_options_alter_workprocess_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work',
            name='processes',
        ),
    ]
