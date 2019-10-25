from django.db import models

class Pregunta(models.Model):
    id_pregunta = models.AutoField(primary_key=True)
    pregunta_texto = models.CharField(blank=False, null=False, max_length=200)
    fecha_publicacion = models.DateField('fecha_de_publicacion', blank=False, null=False)

class Opcion(models.Model):
    id_opcion = models.AutoField(primary_key=True)
    opcion_texto = models.CharField(blank=False, null=False, max_length=200)
    id_fk_pregunta = models.OneToOneField(Pregunta, on_delete= models.CASCADE)
