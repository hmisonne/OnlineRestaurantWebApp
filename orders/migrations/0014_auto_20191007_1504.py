# Generated by Django 2.1.5 on 2019-10-07 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_auto_20191007_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuprice',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Category'),
        ),
    ]
