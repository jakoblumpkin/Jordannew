# Generated by Django 3.1.5 on 2021-02-13 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('release', '0016_auto_20210206_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipping_info',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
