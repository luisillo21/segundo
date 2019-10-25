# Generated by Django 2.2.5 on 2019-10-25 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Opcion',
            fields=[
                ('id_opcion', models.AutoField(primary_key=True, serialize=False)),
                ('opcion_texto', models.CharField(max_length=200)),
                ('id_fk_pregunta', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='polls.Pregunta')),
            ],
        ),
    ]