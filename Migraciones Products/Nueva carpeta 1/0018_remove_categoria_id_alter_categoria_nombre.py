# Generated by Django 5.0.2 on 2024-02-28 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0017_categoria_id_alter_categoria_nombre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='id',
        ),
        migrations.AlterField(
            model_name='categoria',
            name='nombre',
            field=models.CharField(blank=True, default=None, max_length=50, primary_key=True, serialize=False),
        ),
    ]
