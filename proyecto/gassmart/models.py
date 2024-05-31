from django.db import models

class Empresa(models.Model):
    SOLGAS = 'solgas'
    LLAMAGAS = 'llamagas'
    NEWGAS = 'newgas'

    EMPRESA_CHOICES = (
        (SOLGAS, 'Solgas'),
        (LLAMAGAS, 'Llamagas'),
        (NEWGAS, 'Newgas')
    )

    empresa = models.CharField(max_length=10, choices=EMPRESA_CHOICES)
    dirección = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.empresa
    
class Usuario(models.Model):
    usuario = models.CharField(max_length=100)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    dirección = models.CharField(max_length=100)
    
    def __str__(self):
        return self.usuario

class Consumo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    consumo = models.DecimalField(max_digits=6, decimal_places=2)
    costo = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.usuario.usuario} - {self.fecha}"

class Balones(models.Model):
    PREMIUM = 'premium'
    REGULAR = 'regular'
    DIEZ = '10kg'
    QUINCE = '15kg'

    VALVULAS_CHOICES = (
        (PREMIUM, 'Premium'),
        (REGULAR, 'Regular')
    )

    PESO_CHOICES = (
        (DIEZ, '10kg'),
        (QUINCE, '15kg')
    )

    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    valvula = models.CharField(max_length=10, choices=VALVULAS_CHOICES)
    peso = models.CharField(max_length=10, choices=PESO_CHOICES)

    def __str__(self):
        return self.valvula
