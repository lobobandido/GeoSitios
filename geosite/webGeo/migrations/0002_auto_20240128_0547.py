# Generated by Django 3.2 on 2024-01-28 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webGeo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordenservicio',
            name='ingeniero_asig',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='ordenservicio',
            name='sitio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='webGeo.sitio'),
        ),
    ]