# Generated by Django 3.2.4 on 2021-06-21 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_orderupdates'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderUpdates',
            new_name='OrderUpdate',
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='item_json',
            new_name='items_json',
        ),
    ]
