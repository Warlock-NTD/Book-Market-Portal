# Generated by Django 4.0 on 2023-05-12 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_manager', '0004_book_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='genres',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
