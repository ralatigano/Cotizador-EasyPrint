# Generated by Django 5.0.2 on 2024-02-27 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0009_categoria_created_categoria_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='productos',
            field=models.ManyToManyField(blank=True, null=True, related_name='productos', to='Products.producto'),
        ),
    ]