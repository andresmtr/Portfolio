# Generated by Django 3.1.2 on 2022-01-04 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BasePortfolio', '0005_auto_20220104_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.CharField(max_length=150, unique=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='slug',
            field=models.CharField(max_length=150, unique=True, verbose_name='Slug'),
        ),
    ]
