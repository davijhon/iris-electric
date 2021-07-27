# Generated by Django 3.0.7 on 2021-07-26 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0005_medidor'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroMedidor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origen', models.IntegerField(blank=True, choices=[(1, 'SWITCH-SOLICITA'), (2, 'MEDIDOR-RESPUESTA')], null=True)),
                ('kwh', models.DecimalField(decimal_places=2, max_digits=6)),
                ('operador', models.CharField(max_length=100)),
                ('error', models.IntegerField(blank=True, choices=[('OK', 'Sin errores'), ('ERROR', 'Ha ocurrido un error')], null=True)),
                ('observacion', models.CharField(max_length=250)),
                ('fecha_registro', models.DateField(auto_now_add=True)),
                ('hora_registro', models.TimeField(auto_now_add=True)),
                ('medidor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.Medidor')),
            ],
        ),
    ]
