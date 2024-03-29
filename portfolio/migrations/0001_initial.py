# Generated by Django 4.0.4 on 2022-04-21 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=120)),
                ('descripcion', models.CharField(max_length=250)),
                ('imagen', models.ImageField(upload_to='portfolio/fotos')),
                ('camara', models.CharField(max_length=50)),
                ('objetivo', models.CharField(max_length=50)),
                ('obturacion', models.CharField(max_length=10)),
                ('diafragma', models.CharField(max_length=10)),
                ('iso', models.CharField(max_length=10)),
            ],
        ),
    ]
