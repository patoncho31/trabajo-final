# Register your models here.

from django.contrib import admin
from .models import Receta, Categoria


admin.site.register(Receta)
admin.site.register(Categoria)
