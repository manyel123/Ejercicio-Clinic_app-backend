# Generated by Django 3.2.8 on 2021-10-08 15:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=15, unique=True, verbose_name='Username')),
                ('password', models.CharField(max_length=256, verbose_name='Password')),
                ('name', models.CharField(max_length=30, verbose_name='Nombre')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('document', models.IntegerField(verbose_name='Documento')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('document', models.BigIntegerField(verbose_name='Documento')),
                ('name', models.CharField(max_length=30, verbose_name='Nombre')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('fechaNacim', models.CharField(max_length=10, verbose_name='Fecha de Nacimiento')),
                ('telefono', models.IntegerField(verbose_name='Telefono')),
                ('direccion', models.CharField(max_length=30, verbose_name='Direccion')),
                ('ciudad', models.CharField(max_length=20, verbose_name='Ciudad')),
            ],
        ),
        migrations.CreateModel(
            name='Historia',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('ultMedTrat', models.CharField(max_length=30, verbose_name='Ultimo medico tratante')),
                ('antQuirurgicos', models.CharField(max_length=100, verbose_name='Antecedentes quirurgicos')),
                ('antMedicos', models.CharField(max_length=100, verbose_name='Antecedentes medicos')),
                ('antFarmacologicos', models.CharField(max_length=100, verbose_name='Antecedentes farmacologicos')),
                ('tratamientoFarmacol', models.CharField(max_length=100, verbose_name='Tratamiento farmacologico actual')),
                ('diagPrevio', models.CharField(max_length=100, verbose_name='Diagnostico previo')),
                ('diagActual', models.CharField(max_length=100, verbose_name='Diagnostico actual')),
                ('observacion', models.TextField(max_length=10000, verbose_name='Observaciones')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paciente', to='authApp.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('fechaCita', models.CharField(max_length=10, verbose_name='Fecha de Cita')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paciente_id', to='authApp.paciente')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]