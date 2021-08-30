# Generated by Django 3.2.6 on 2021-08-29 22:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('slug', models.SlugField(default='Nada')),
            ],
            options={
                'db_table': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True, help_text='Fecha de creación', verbose_name='creado')),
                ('modificado', models.DateTimeField(auto_now=True, help_text='Fecha de modificación', verbose_name='modificado')),
                ('nombre', models.CharField(max_length=50)),
                ('dificultad', models.CharField(choices=[('1', 'Fácil'), ('2', 'Medio'), ('3', 'Difícil')], default='1', max_length=1)),
                ('datoObligatorio', models.BooleanField(default=False)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='preguntas.categoria')),
            ],
            options={
                'db_table': 'Preguntas',
            },
        ),
        migrations.CreateModel(
            name='OpcionPregunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consigna', models.CharField(max_length=250)),
                ('correcta', models.BooleanField(default=False)),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='preguntas.pregunta')),
            ],
            options={
                'db_table': 'Opciones_Preguntas',
            },
        ),
    ]
