# Generated by Django 3.2.6 on 2021-09-02 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preguntas', '0003_alter_pregunta_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pregunta',
            name='dificultad',
            field=models.CharField(choices=[('1', 'Fácil'), ('2', 'Media'), ('3', 'Difícil')], default='1', max_length=1),
        ),
    ]