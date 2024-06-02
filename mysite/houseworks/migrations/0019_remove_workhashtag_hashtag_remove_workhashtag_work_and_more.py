# Generated by Django 5.0.4 on 2024-06-02 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houseworks', '0018_alter_workschedule_schedule'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workhashtag',
            name='hashtag',
        ),
        migrations.RemoveField(
            model_name='workhashtag',
            name='work',
        ),
        migrations.AlterField(
            model_name='work',
            name='next_execute_date',
            field=models.DateField(verbose_name='次回予定日'),
        ),
        migrations.DeleteModel(
            name='HashTag',
        ),
        migrations.DeleteModel(
            name='WorkHashtag',
        ),
    ]