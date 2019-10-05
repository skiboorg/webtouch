# Generated by Django 2.2.6 on 2019-10-05 17:40

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='portfolioitem',
            options={'verbose_name': 'Кейс', 'verbose_name_plural': 'Кейсы'},
        ),
        migrations.AddField(
            model_name='portfolioitem',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='portfolioitem',
            name='is_active',
            field=models.BooleanField(db_index=True, default=True, verbose_name='Отображать на главной?'),
        ),
    ]
