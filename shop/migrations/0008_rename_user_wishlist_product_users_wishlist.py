# Generated by Django 3.2.9 on 2022-05-29 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_product_user_wishlist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='user_wishlist',
            new_name='users_wishlist',
        ),
    ]
