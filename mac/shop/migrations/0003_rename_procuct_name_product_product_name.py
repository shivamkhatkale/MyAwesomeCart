# Generated by Django 4.1 on 2022-08-25 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_category_product_image_product_price_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='procuct_name',
            new_name='product_name',
        ),
    ]
