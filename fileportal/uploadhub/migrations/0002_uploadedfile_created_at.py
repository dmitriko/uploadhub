# Generated by Django 4.2.7 on 2023-11-11 19:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('uploadhub', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedfile',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
