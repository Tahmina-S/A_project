# Generated by Django 4.2.7 on 2023-11-25 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase_model',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
