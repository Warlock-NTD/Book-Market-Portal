# Generated by Django 4.0 on 2023-05-13 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_manager', '0006_alter_book_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='genres',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=1024, null=True),
        ),
    ]
