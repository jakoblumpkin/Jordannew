# Generated by Django 3.1.5 on 2021-02-06 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('release', '0011_auto_20210205_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='item',
            field=models.ManyToManyField(null=True, to='release.Items'),
        ),
    ]
