# Generated by Django 3.1.5 on 2021-02-06 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('release', '0006_items_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='item',
            field=models.ManyToManyField(to='release.Items'),
        ),
    ]
