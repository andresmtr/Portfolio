# Generated by Django 3.1.2 on 2022-04-27 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BasePortfolio', '0029_auto_20220427_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='descriptionJob',
            field=models.TextField(verbose_name='description'),
        ),
    ]