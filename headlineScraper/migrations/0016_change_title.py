# Generated by Django 2.1.4 on 2019-07-12 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('headlineScraper', '0015_change_pos'),
    ]

    operations = [
        migrations.AddField(
            model_name='change',
            name='title',
            field=models.BooleanField(default=False),
        ),
    ]
