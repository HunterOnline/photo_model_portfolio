# Generated by Django 3.2.9 on 2022-08-10 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_page', '0003_auto_20220810_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='description',
            field=models.TextField(max_length=1000, verbose_name='Опис'),
        ),
    ]
