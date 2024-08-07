# Generated by Django 5.0.6 on 2024-07-31 09:41

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info_assist', '0005_remove_documentinfo_path_doc_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdfdatabase',
            name='blob',
            field=models.BinaryField(blank=True, null=True, verbose_name='PDF файл'),
        ),
        migrations.AddField(
            model_name='pdfdatabase',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания'),
        ),
        migrations.AddField(
            model_name='pdfdatabase',
            name='status',
            field=models.CharField(blank=True, max_length=255, verbose_name='Статус'),
        ),
        migrations.AddField(
            model_name='pdfdatabase',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата обновления'),
        ),
    ]
