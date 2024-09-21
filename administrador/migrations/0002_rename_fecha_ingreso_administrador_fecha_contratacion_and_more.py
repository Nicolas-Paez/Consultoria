# Generated by Django 5.1 on 2024-09-20 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='administrador',
            old_name='fecha_ingreso',
            new_name='fecha_contratacion',
        ),
        migrations.RemoveField(
            model_name='administrador',
            name='estado',
        ),
        migrations.AddField(
            model_name='administrador',
            name='departamento',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
