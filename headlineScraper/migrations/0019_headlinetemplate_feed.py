# Generated by Django 2.1.4 on 2019-07-14 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('headlineScraper', '0018_auto_20190713_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='headlinetemplate',
            name='feed',
            field=models.TextField(default=None, null=True),
        ),
    ]
