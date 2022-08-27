# Generated by Django 3.2.5 on 2022-08-27 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendario', '0002_auto_20220826_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateTimeField(verbose_name='Fecha del evento'),
        ),
        migrations.AlterField(
            model_name='event',
            name='manager',
            field=models.CharField(max_length=60, verbose_name='Encargado'),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=120, verbose_name='Evento'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=30, verbose_name='Apellido'),
        ),
    ]