# Generated by Django 4.0.6 on 2022-09-21 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_book_id_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, upload_to='covers/'),
        ),
    ]