# Generated by Django 2.1.5 on 2019-10-07 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0016_auto_20191007_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuprice',
            name='topping_qty',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
