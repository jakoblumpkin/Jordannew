# Generated by Django 3.1.5 on 2021-02-07 00:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('release', '0014_auto_20210206_1039'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='shippinginfo',
            new_name='shipping_info',
        ),
    ]