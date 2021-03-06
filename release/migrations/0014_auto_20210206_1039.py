# Generated by Django 3.1.5 on 2021-02-06 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('release', '0013_auto_20210206_0953'),
    ]

    operations = [
        migrations.CreateModel(
            name='shippinginfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('zipcode', models.CharField(max_length=20)),
                ('citystate', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='shipping',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='release.shippinginfo'),
        ),
    ]
