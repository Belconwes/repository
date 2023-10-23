from django.db import models
from django.core.validators import MinValueValidator
from Aplications.Usuarios.models import User

# Create your models here.
class Categoria (models.Model):
    nombre = models.CharField('Nombre', max_length=30,)    # blank=True (permite vacios) | Max_length ancho  | El 1er valor es la etiqueta
    sigla = models.CharField('Sigla', max_length=10,)    # Por defecto NO permite  #El blank si permite o no blancos
    # default='ValorPredeterminado' (hace que inicie con ese valor)
    class Meta:
        verbose_name = 'Categoria'    # Para cambiar el nombre de la clase en singular
        verbose_name_plural = ('Categorias')   # Para cambiar el nombre de la clase en plural
        ordering = ['nombre']  # Se debe poner dentro de las comillas la var del atributo
        unique_together = ('nombre', 'sigla')
    
    def __str__(self):
        return self.sigla+' - '+self.nombre
    

class Producto (models.Model):
    #Modelo de producto
    MEDIDAS_CHOICES =(
        ('0', 'Grs'),
        ('1', 'Kgs'),
        ('2', 'Cm3'),
        ('3', 'Mls'),
        ('4', 'Lts'),
    )
    nombre = models.CharField('Nombre', max_length=50)
    id = models.CharField('ID', max_length=50, primary_key=True)
    medida = models.DecimalField('Medida', max_digits=6, decimal_places=2)
    tipo_medida = models.CharField('Tipo de medida', max_length=1, choices=MEDIDAS_CHOICES)
    descripcion = models.TextField('Descripción')  # Campo de texto largo
    precio = models.DecimalField('Precio ($)', max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])  # Campo decimal (10 digitos incluyendo dec)(2 decimales)
    detail_image = models.ImageField(upload_to='products',null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField('cantidad', null= True)
    
    
    # Relacion entre producto y categoria (De muchos a 1)
    # Para elegir el nombre personalizado desde la vista del administrador de stock
    
    class Meta:
        verbose_name = ('Producto')
        verbose_name_plural = ('Productos')
        ordering = ['nombre']
        unique_together = ('nombre', 'id', 'tipo_medida', 'medida')
    
    def __str__(self):
        return self.id+' - '+self.nombre
    



