# Generated by Django 5.0.2 on 2024-03-13 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_pedido_id_alter_pedido_estado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='estado',
            field=models.TextField(choices=[('Sin seña', 'Sin seña'), ('Señado', 'Señado'), ('En proceso', 'En proceso'), ('Para retirar', 'Para retirar'), ('Entregado', 'Entregado'), ('Pagado', 'Pagado'), ('Cancelado', 'Cancelado')], default='Sin seña', max_length=100),
        ),
    ]
