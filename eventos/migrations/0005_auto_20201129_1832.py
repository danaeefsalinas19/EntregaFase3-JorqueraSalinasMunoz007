# Generated by Django 3.1.2 on 2020-11-29 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0004_auto_20201129_1802'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reserva',
            old_name='codigo_reserva',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='servicio',
            old_name='codigo_servicio',
            new_name='id',
        ),
    ]
