# Generated by Django 2.0.3 on 2018-04-01 16:00

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopuser',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(default='', max_length=128, verbose_name='номер телефона'),
        ),
    ]