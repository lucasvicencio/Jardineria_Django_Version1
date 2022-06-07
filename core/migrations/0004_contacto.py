# Generated by Django 4.0.5 on 2022-06-06 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_marca'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('tipo_consulta', models.IntegerField(choices=[[0, 'Consultas'], [1, 'Reclamo'], [2, 'Sugerencia'], [3, 'Felicitaciones']])),
                ('mensaje', models.TextField()),
                ('avisos', models.BooleanField()),
            ],
        ),
    ]
