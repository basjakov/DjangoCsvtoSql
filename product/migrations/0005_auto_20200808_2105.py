# Generated by Django 3.0.5 on 2020-08-08 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20200801_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='count',
            field=models.CharField(max_length=13),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(max_length=13),
        ),
    ]
