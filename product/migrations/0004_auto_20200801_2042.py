# Generated by Django 3.0.5 on 2020-08-01 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20200801_1730'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='total',
            new_name='price',
        ),
    ]
