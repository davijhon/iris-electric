# Generated by Django 3.0.7 on 2021-07-23 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regional',
            name='dia_lectura',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='regional',
            name='horario_lectura',
            field=models.TimeField(),
        ),
    ]