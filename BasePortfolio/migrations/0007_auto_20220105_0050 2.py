# Generated by Django 3.1.2 on 2022-01-05 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BasePortfolio', '0006_auto_20220104_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(max_length=255, upload_to='projects/', verbose_name='Image'),
        ),
    ]
