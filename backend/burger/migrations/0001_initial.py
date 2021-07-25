# Generated by Django 3.2.5 on 2021-07-19 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('servicio', models.CharField(max_length=100)),
                ('pago', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('imagen', models.TextField()),
                ('tipo', models.CharField(max_length=100)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CxP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unidad', models.IntegerField()),
                ('IdCustomer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='burger.customer')),
                ('IdProduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='burger.product')),
            ],
        ),
    ]
