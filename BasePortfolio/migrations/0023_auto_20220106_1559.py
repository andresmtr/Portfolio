# Generated by Django 3.1.2 on 2022-01-06 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BasePortfolio', '0022_auto_20220106_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdf',
            name='date_updatePdf',
            field=models.DateField(blank=True, null=True, verbose_name='Date of Creation'),
        ),
    ]
