# Generated by Django 3.1.2 on 2020-11-30 23:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0013_reserva_comentarios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='id',
            field=models.CharField(default=uuid.uuid4, max_length=200, primary_key=True, serialize=False),
        ),
    ]
