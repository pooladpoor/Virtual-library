# Generated by Django 5.1 on 2024-08-20 20:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0009_delete_borrow'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_deadline', models.DateTimeField(auto_now_add=True)),
                ('e_deadline', models.DateTimeField(blank=True, null=True)),
                ('Borrower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Borrows', to=settings.AUTH_USER_MODEL)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Borrows', to='home.book')),
            ],
        ),
    ]
