# Generated by Django 5.1 on 2024-08-20 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_book_summary_book_is_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='Summary',
            field=models.TextField(blank=True, default='Book summary is not available'),
        ),
    ]
