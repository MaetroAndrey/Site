# Generated by Django 3.2 on 2021-05-13 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_news_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='view',
            field=models.IntegerField(default=0),
        ),
    ]
