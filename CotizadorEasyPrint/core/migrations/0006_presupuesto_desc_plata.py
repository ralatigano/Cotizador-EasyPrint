# Generated by Django 5.0.2 on 2024-03-18 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_pedido_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='presupuesto',
            name='desc_plata',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
