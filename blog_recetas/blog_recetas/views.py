from django.shortcuts import render
from django.views import View

def Home_recetas(request):
      # Lógica de la vista aquí
        return render(request, 'home_recetas.html')
    
    
def Nosotros(request):
    return render(request, 'nosotros.html')