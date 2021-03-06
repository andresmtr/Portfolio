# Generated by Django 3.1.2 on 2022-01-03 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BasePortfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(max_length=255, null=True, upload_to='projects/', verbose_name='Image'),
        ),
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='State')),
                ('date_modify', models.DateField(auto_now=True, verbose_name='Date of Modify')),
                ('date_delete', models.DateField(auto_now=True, verbose_name='Date of Delete')),
                ('title', models.CharField(max_length=150, unique=True, verbose_name='Title')),
                ('description', models.TextField(verbose_name='description')),
                ('GitLink', models.URLField(blank=True, null=True, verbose_name='Github repository')),
                ('YoutubeLink', models.URLField(blank=True, null=True, verbose_name='Youtube')),
                ('PythonanywhereLink', models.URLField(blank=True, null=True, verbose_name='Pythonanywhere')),
                ('image', models.ImageField(max_length=255, null=True, upload_to='tutorials/', verbose_name='Image')),
                ('date_creaction', models.DateField(verbose_name='Date of Creation')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BasePortfolio.author')),
            ],
            options={
                'verbose_name': 'Tutorial',
                'verbose_name_plural': 'Tutorials',
            },
        ),
    ]
