# Generated by Django 3.0.5 on 2020-08-01 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product',
            field=models.CharField(choices=[('Ershik', 'ershik'), ('Paxpaxak', 'paxpaxak'), ('Pnduk', 'pnduk'), ('Chocolate', 'chocolate')], max_length=11),
        ),
        migrations.AlterField(
            model_name='product',
            name='productowner',
            field=models.CharField(max_length=13),
        ),
    ]
