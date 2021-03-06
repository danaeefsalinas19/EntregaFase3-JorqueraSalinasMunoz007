# Generated by Django 3.1.2 on 2020-10-20 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='reserva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_reserva', models.CharField(max_length=10)),
                ('fecha_evento', models.DateField(blank=True, null=True)),
                ('nom_cliente', models.CharField(max_length=200)),
                ('apell_cliente', models.CharField(max_length=200)),
                ('celu_cliente', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=200)),
                ('cant_personas', models.IntegerField(default=0)),
                ('total', models.IntegerField(default=0)),
            ],
        ),
        
        migrations.CreateModel(
            name='servicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_servicio', models.CharField(max_length=10)),
                ('nom_servicio', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=200)),
                ('precio_por_persona', models.CharField(max_length=10)),
            ],
        ),
    
        
    ]

    