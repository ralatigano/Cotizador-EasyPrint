# Generated by Django 5.0.2 on 2024-02-27 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0008_alter_producto_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='categoria',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
    ]