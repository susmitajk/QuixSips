# Generated by Django 5.0.3 on 2024-04-18 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_productimage_is_deleted_productvariant_is_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
