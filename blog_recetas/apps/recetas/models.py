from django.db import models
from apps.usuarios.models import Usuario


# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Receta(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    ingredientes = models.TextField()
    instrucciones = models.TextField() 
    imagen = models.ImageField(upload_to="recetas", null=True)
    fecha_publicacion= models.DateTimeField(auto_now_add=True, editable=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL,null=True)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, null = True)
    
    def __str__(self):
        return self.titulo
        

class Comentario(models.Model):
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE, related_name='comentarios')
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario = models.CharField(max_length=50)

    def __str__(self):
        return self.contenido

    
