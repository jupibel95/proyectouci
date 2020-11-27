from django.db import models

# Create your models here.

class Centro_asistencial(models.Model):
    nombre = models.CharField(max_length=64)
    nit = models.IntegerField()
    numero_de_camas_en_uci = models.IntegerField(max_length=10)
    numero_de_camas_ocupadas_en_uci = models.IntegerField(max_length=10)
    numero_de_camas_disponibles_en_uci = models.IntegerField(max_length=10)

    def __str__(self) -> str:
        return str(self.nit) + "-" + self.nombre




# Create your models here.
class Ubicacion(models.Model):
    nombre = models.CharField(max_length=64)
    direccion = models.CharField(max_length=64)
    centro_asistencial = models.ForeignKey(Centro_asistencial, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return str(self.direccion)