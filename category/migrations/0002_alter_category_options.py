# Generated by Django 5.0.3 on 2024-06-10 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-id'], 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]
