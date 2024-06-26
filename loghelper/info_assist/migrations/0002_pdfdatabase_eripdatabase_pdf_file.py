# Generated by Django 5.0.6 on 2024-06-27 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info_assist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PDFDataBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_number', models.CharField(max_length=70, unique=True, verbose_name='Номер уведомления')),
                ('full_path', models.CharField(blank=True, max_length=255, verbose_name='Полный путь')),
                ('file_name', models.CharField(blank=True, max_length=30, verbose_name='Имя файла')),
                ('in_use', models.BooleanField(default=False, verbose_name='Путь найден')),
            ],
        ),
        migrations.AddField(
            model_name='eripdatabase',
            name='pdf_file',
            field=models.FileField(blank=True, null=True, upload_to='pdfs/', verbose_name='PDF файл'),
        ),
    ]
