# Generated by Django 5.0.6 on 2024-08-01 12:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info_assist', '0008_alter_pdfdatabase_doc_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdfdatabase',
            name='document',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pdf_file', to='info_assist.documentinfo'),
        ),
    ]
