# Generated by Django 3.1.2 on 2021-09-23 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sales',
            name='items_json',
        ),
    ]
