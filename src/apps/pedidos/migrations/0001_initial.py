# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-04 19:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0002_userprofile_cart'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('numero_pedido', models.CharField(default='00001', max_length=12, unique=True, verbose_name='Código de Pedido')),
                ('precio_total', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Precio Total')),
                ('cart', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cart.Cart')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pedidos', to='usuarios.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='PedidoItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_price_base', models.DecimalField(decimal_places=2, max_digits=18, verbose_name='unit base price')),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=18, verbose_name='unit price')),
                ('quantity', models.PositiveIntegerField(verbose_name='Cantidad')),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=18, verbose_name='Total')),
                ('object_id', models.PositiveIntegerField()),
                ('fecha', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de compra')),
                ('producto', models.CharField(blank=True, max_length=200, verbose_name='Producto/Servicio')),
                ('presentacion', models.CharField(blank=True, max_length=200, verbose_name='Presentacion')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pedido_item', to='pedidos.Pedido', verbose_name='Pedido')),
            ],
            options={
                'verbose_name_plural': 'items',
                'ordering': ('pedido',),
                'verbose_name': 'item',
            },
        ),
    ]