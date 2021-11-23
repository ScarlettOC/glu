from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
from django.contrib.auth.models import User

#Implementar Modelos

class Client(models.Model):
    names = models.CharField(max_length=150, verbose_name='Nombres')
    surnames = models.CharField(max_length=150, verbose_name='Apellidos')
    dni = models.CharField(max_length=10, unique=True, verbose_name='Dni')
    birthday = models.DateField(default=datetime.now, verbose_name='Fecha de nacimiento')
    address = models.CharField(max_length=150, null=True, blank=True, verbose_name='Dirección')
    SEXO = (('F', 'Femenino'),('M', 'Masculino'))
    genero = models.CharField(max_length=12, choices=SEXO, blank=False, default='F')

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']



class Registro(models.Model):
    #cliente = models.ForeignKey(Client, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=20)
    SENTIMIENTO = (('Miedo', 'Miedo'),('Alegria', 'Alegria'),('Tristeza', 'Tristeza'),('Enojo', 'Enojo'),('Afecto', 'Afecto'))
    sentimiento = models.CharField(max_length=12, choices=SENTIMIENTO, blank=False, default='Mi')
    nota = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='static/images/',null=True)


    def __str__(self):
        return self.names

    def toJSON(self):
        item = model_to_dict(self)
        item['usuario']=self.cliente.toJSON()
        item['nombre']=format(self.nombre,'.2f')
        item['nota']=format(self.nota,'.2f')
        item['created_at']=sel.created_at.strftime('%Y-%m-%d')
        item['updated_at']=sel.updated_at.strftime('%Y-%m-%d')
        item['det']=[i.toJSON() for i in self.detsen_set.all()]
        return item


class Sale(models.Model):
    cliente = models.ForeignKey(Client, on_delete=models.CASCADE)
    registro = models.ForeignKey(Registro, on_delete=models.CASCADE)
 
    def __str__(self):
        return self.cliente.registro

    def toJSON(self):
        item = model_to_dict(self)
        item['cliente'] = self.cliente.toJSON()
        item['registro'] = self.registro.toJSON()
        item['det'] = [i.toJSON() for i in self.detsale_set.all()]
        return item

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['id']
