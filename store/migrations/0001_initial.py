# Generated by Django 5.0.3 on 2024-04-03 13:01

import django.db.models.deletion
import store.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('is_deleted', models.BooleanField(default=False)),
                ('image', models.ImageField(upload_to='photos/products')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brand_products', to='store.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
                ('liquor_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.type')),
            ],
        ),
        migrations.CreateModel(
            name='ProductVariant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('age', models.PositiveIntegerField(validators=[store.models.validate_age_within_range])),
                ('proof', models.DecimalField(decimal_places=2, max_digits=5, validators=[store.models.validate_proof_within_range])),
                ('volume', models.DecimalField(decimal_places=2, max_digits=5, validators=[store.models.validate_volume_within_range])),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, validators=[store.models.validate_price_within_range])),
                ('stock', models.PositiveIntegerField(validators=[store.models.validate_stock_within_range])),
                ('is_active', models.BooleanField(default=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='store.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photos/productvariant')),
                ('variant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='store.productvariant')),
            ],
        ),
    ]