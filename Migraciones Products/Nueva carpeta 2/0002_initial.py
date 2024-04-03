# Generated by Django 5.0.2 on 2024-02-28 13:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Products', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='presupuesto',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.presupuesto'),
        ),
    ]
