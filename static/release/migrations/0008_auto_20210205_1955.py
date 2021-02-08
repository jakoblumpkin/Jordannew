# Generated by Django 3.1.5 on 2021-02-06 01:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('release', '0007_user_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='item',
        ),
        migrations.AddField(
            model_name='user',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='release.items'),
        ),
    ]