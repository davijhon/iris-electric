# Generated by Django 3.0.7 on 2021-07-26 13:14

from django.db import migrations
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0002_auto_20210723_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='suministro',
            name='location',
            field=location_field.models.plain.PlainLocationField(default=1, max_length=63),
            preserve_default=False,
        ),
    ]