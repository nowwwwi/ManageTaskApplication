# Generated by Django 5.0.4 on 2024-05-06 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houseworks', '0007_alter_weekdaysofwork_options_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='WorkType',
            new_name='HashTag',
        ),
        migrations.AlterModelOptions(
            name='hashtag',
            options={'verbose_name': 'ハッシュタグ', 'verbose_name_plural': 'ハッシュタグ'},
        ),
        migrations.RemoveField(
            model_name='work',
            name='work_type',
        ),
        migrations.AddField(
            model_name='work',
            name='hashtags',
            field=models.ManyToManyField(blank=True, related_name='works', to='houseworks.hashtag'),
        ),
    ]