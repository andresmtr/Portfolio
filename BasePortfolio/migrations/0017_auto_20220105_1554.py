# Generated by Django 3.1.2 on 2022-01-05 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BasePortfolio', '0016_auto_20220105_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date_creaction_project',
            field=models.DateField(blank=True, null=True, verbose_name='Date of Creation'),
        ),
    ]
