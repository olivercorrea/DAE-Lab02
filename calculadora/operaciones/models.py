from django.db import models

# Create your models here.

class Operacion(models.Model):
    numero1 = models.IntegerField()
    numero2 = models.IntegerField()
    operacion = models.CharField(max_length=15, choices=[('suma', 'Suma'), ('resta', 'Resta'), ('multiplicacion', 'Multiplicación')])

    def __str__(self):
        return f'{self.numero1} {self.operacion} {self.numero2}'
    
