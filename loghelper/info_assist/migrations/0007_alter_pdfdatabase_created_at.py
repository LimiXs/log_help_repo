# Generated by Django 5.0.6 on 2024-07-31 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info_assist', '0006_pdfdatabase_blob_pdfdatabase_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdfdatabase',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
    ]
