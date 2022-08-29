# Generated by Django 3.2.9 on 2022-08-24 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_page', '0004_alter_news_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='bio',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='myphoto',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='news',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='photoalbum',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='video',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
    ]