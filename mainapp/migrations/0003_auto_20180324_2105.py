# Generated by Django 2.0.3 on 2018-03-24 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='vendor_id',
            field=models.CharField(blank=True, max_length=10, unique=True, verbose_name='Артикул'),
        ),
    ]