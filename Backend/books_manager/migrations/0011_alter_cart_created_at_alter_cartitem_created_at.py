# Generated by Django 4.0 on 2023-05-16 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_manager', '0010_cart_alter_rating_user_cartitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
