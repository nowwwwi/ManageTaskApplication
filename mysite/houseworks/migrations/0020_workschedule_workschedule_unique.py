# Generated by Django 5.0.4 on 2024-06-02 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houseworks', '0019_remove_workhashtag_hashtag_remove_workhashtag_work_and_more'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='workschedule',
            constraint=models.UniqueConstraint(fields=('work', 'schedule'), name='workschedule_unique'),
        ),
    ]
