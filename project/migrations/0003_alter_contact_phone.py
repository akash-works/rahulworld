# Generated by Django 4.1.7 on 2023-03-29 12:35

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_alter_contact_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=12, null=True),
        ),
    ]
