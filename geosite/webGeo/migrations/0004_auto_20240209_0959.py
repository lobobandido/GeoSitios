# Generated by Django 3.2 on 2024-02-09 15:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('webGeo', '0003_sitio_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordenservicio',
            name='fecha_registro',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sitio',
            name='fecha_registro',
            field=models.DateTimeField(auto_now_add=True, default='2024-02-07'),
            preserve_default=False,
        ),
    ]
