# Generated by Django 5.0.6 on 2024-06-03 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(upload_to='books/images/covers/'),
        ),
    ]
