# Generated by Django 5.0.2 on 2024-03-31 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_pedido_encargado'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='direccion',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
    ]
