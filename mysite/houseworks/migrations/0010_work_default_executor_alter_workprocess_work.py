# Generated by Django 5.0.4 on 2024-05-10 03:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houseworks', '0009_intervaltype_remove_work_is_regular_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='default_executor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='デフォルトの担当者'),
        ),
        migrations.AlterField(
            model_name='workprocess',
            name='work',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_processes', to='houseworks.work', verbose_name='家事'),
        ),
    ]
