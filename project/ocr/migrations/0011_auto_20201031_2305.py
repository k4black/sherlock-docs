# Generated by Django 3.0.4 on 2020-10-31 20:05

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocr', '0010_documenttype_attributes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='file_type',
        ),
        migrations.RemoveField(
            model_name='document',
            name='type',
        ),
        migrations.RemoveField(
            model_name='pagedocument',
            name='jpg_file',
        ),
        migrations.AddField(
            model_name='pagedocument',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, verbose_name='Атрибуты документа'),
        ),
        migrations.AlterField(
            model_name='document',
            name='status',
            field=models.CharField(choices=[('Q', 'В очереди'), ('P', 'В процессе'), ('C', 'Распознан'), ('F', 'Не распознан')], default='Q', max_length=1, verbose_name='Статус распознавания'),
        ),
        migrations.AlterField(
            model_name='pagedocument',
            name='status',
            field=models.CharField(choices=[('Q', 'В очереди'), ('P', 'В процессе'), ('C', 'Распознан'), ('F', 'Не распознан')], default='Q', max_length=1, verbose_name='Статус распознавания'),
        ),
        migrations.DeleteModel(
            name='FormalizedDocument',
        ),
    ]
