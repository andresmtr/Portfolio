# Generated by Django 3.1.2 on 2022-01-05 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BasePortfolio', '0011_auto_20220105_1525'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='date_creaction_project',
        ),
        migrations.AlterField(
            model_name='project',
            name='date_creaction',
            field=models.DateField(verbose_name='Date of Creation'),
        ),
    ]
