# Generated by Django 5.2 on 2025-05-05 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='base_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='expense',
            name='currency',
            field=models.CharField(default='USD', max_length=3),
        ),
    ]
