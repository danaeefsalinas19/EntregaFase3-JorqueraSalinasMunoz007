# Generated by Django 3.1.2 on 2020-11-30 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0005_auto_20201129_1832'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]