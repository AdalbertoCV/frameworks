# Generated by Django 4.1.4 on 2023-03-10 01:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('materias', '0003_alter_materia_semestre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('matricula', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='matricula')),
                ('nombre', models.CharField(max_length=50, verbose_name='nombre')),
                ('apellidoPaterno', models.CharField(max_length=50, verbose_name='apellidopaterno')),
                ('apellidoMaterno', models.CharField(max_length=50, verbose_name='apellidomaterno')),
            ],
        ),
        migrations.CreateModel(
            name='Hora',
            fields=[
                ('clave', models.IntegerField(primary_key=True, serialize=False, verbose_name='clave')),
                ('horaInicio', models.CharField(max_length=5, verbose_name='horainicio')),
                ('horaFin', models.CharField(max_length=5, verbose_name='horafin')),
            ],
        ),
        migrations.CreateModel(
            name='Salon',
            fields=[
                ('clave', models.IntegerField(primary_key=True, serialize=False, verbose_name='clave')),
                ('nombre', models.CharField(max_length=50, verbose_name='nombre')),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clave', models.IntegerField(verbose_name='Clave')),
                ('semestre', models.CharField(choices=[('', '-------------'), ('1', '1er Semestre'), ('2', '2do Semestre'), ('3', '3er Semestre'), ('4', '4to Semestre'), ('5', '5to Semestre'), ('6', '6to Semestre'), ('7', '7mo Semestre'), ('8', '8vo Semestre'), ('9', '9no Semestre')], max_length=2)),
                ('dia', models.CharField(choices=[('', '-------------'), ('1', 'Lunes'), ('2', 'Martes'), ('3', 'Miércoles'), ('4', 'Jueves'), ('5', 'Viernes'), ('6', 'Sábado')], max_length=2)),
                ('docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='horarios.docente', verbose_name='Docente')),
                ('hora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='horarios.hora', verbose_name='Hora')),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materias.materia', verbose_name='Materia')),
                ('salon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='horarios.salon', verbose_name='Salon')),
            ],
        ),
    ]