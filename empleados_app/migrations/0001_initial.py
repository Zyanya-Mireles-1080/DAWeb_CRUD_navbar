# Generated by Django 5.1 on 2024-11-27 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('id_empleado', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
                ('correo', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=30)),
                ('turno', models.CharField(max_length=30)),
                ('sueldo', models.IntegerField()),
            ],
        ),
    ]
