# Generated by Django 5.1.5 on 2025-02-27 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='create_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
