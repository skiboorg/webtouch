# Generated by Django 2.2.6 on 2019-10-05 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20191005_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolioitemimage',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='porfolioItemImages', to='pages.PortfolioItem', verbose_name='Кейс'),
        ),
    ]
