# Generated by Django 4.0 on 2023-05-10 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_manager', '0002_user_age_user_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]