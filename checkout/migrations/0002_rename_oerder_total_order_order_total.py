# Generated by Django 3.2.23 on 2024-02-11 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='oerder_total',
            new_name='order_total',
        ),
    ]