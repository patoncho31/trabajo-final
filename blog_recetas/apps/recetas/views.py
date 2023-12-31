from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Receta, Categoria, Comentario
from .forms import RecetaForm, ComentarioForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib import messages

def ListarRecetas(request):
      # Lógica de la vista aquí
    contexto = {}
    
    
    id_categoria= request.GET.get("id",None)

    if id_categoria:
          n = Receta.objects.filter(categoria = id_categoria)
    else:
          n = Receta.objects.all() # SELECT * FROM RECETAS
          
    cat = Categoria.objects.all().order_by('nombre') #ordena por nombre
    contexto['recetas'] = n
    contexto['categorias'] = cat
    
    #Filtra por Fecha de Publicacion
    #Ascendente
    
    antiguedad_asc = request.GET.get("antiguedad_asc")
    if antiguedad_asc:
        n = Receta.objects.all().order_by('fecha_publicacion') #ordena por fecha


    # filtrar por antiguedad desc
    
    antiguedad_desc = request.GET.get("antiguedad_desc")
    if antiguedad_desc:
        n = Receta.objects.all().order_by('-fecha_publicacion') #ordena por fecha

            
       # filtrar por orden alfabetico asc
    
    orden_asc = request.GET.get("orden_asc")
    if orden_asc:
        n = Receta.objects.all().order_by('titulo') #ordena por titulo


    # filtrar por orden alfabetico desc
    orden_desc = request.GET.get("orden_desc")
    if orden_desc:
        n = Receta.objects.all().order_by('-titulo') #ordena por titulo

      
    return render(request, 'recetas/listar.html', contexto)
    
    
def DetalleReceta(request, pk):
    
    contexto = {}

    n = Receta.objects.get(pk = pk) # SELECT * FROM NOTICIAS WHERE id = 1
    c = n.comentarios.all()
    
    contexto['receta'] = n
    
        
      #BORRAR NOTICIA
    if request.method == 'POST' and 'delete_receta' in request.POST:
        n.delete()
        return redirect('recetas:listar')
    
       
        
    #COMENTARIO
          
    if request.method == 'POST' and 'add_comentario' in request.POST:
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.user
            form.save()
            return redirect('recetas:detalle', pk=pk)
    else:
        form = ComentarioForm()
    
   
    contexto = {
        'receta': n,
        'comentarios': c,
        'form': form,
    }




   
    return render (request, 'recetas/detalle.html', contexto)



@login_required
def AddReceta(request):
    if request.method == 'POST':
        form = RecetaForm(request.POST or None, request.FILES) ##Request files es para las imagenes


        if form.is_valid():
            receta = form.save(commit=False)
            receta.autor = request.user
            form.save()
            return redirect('home')
    else:
        form = RecetaForm()
   
    return render (request, 'receta/addReceta.html', {'form':form})


@login_required
def AddComentario(request, receta_id):

    receta = get_object_or_404(Receta, id = receta_id)  
    if request.method == 'POST':
        contenido = request.POST.get("contenido")
        usuario = request.user.username
        # creacion de comentario
        Comentario.objects.create(receta = receta, usuario = usuario, contenido = contenido)
        
    return redirect('recetas:detalle', pk = receta_id)

@login_required
def BorrarComentario(request, comentario_id):

    comentario = get_object_or_404(Comentario, id = comentario_id)   
    if comentario.usuario == request.user.username:
        comentario.delete()
    
    return redirect('recetas:detalle', pk = comentario.receta.pk)


# EDITAR COMENTARIOS
@login_required #debes estar loggeado para poder editar
def EditarComentario(request, comentario_id):
    comentario = get_object_or_404(Comentario, id=comentario_id)

    # mensaje de error si no sos el autor del comentario
    #if comentario.usuario != request.user.username:
        #messages.error(request, 'No tenes permiso para editar este comentario')
        #return redirect('noticias:detalle', pk=comentario.noticia.pk)
    
    if request.method == 'POST':
        form = ComentarioForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            return redirect('recetas:detalle', pk=comentario.receta.pk)
    else:
        form = ComentarioForm(instance=comentario)
    
    contexto = {
        'form':form,
        'comentario':comentario,
    }

    return render(request, 'recetas/editar_comentario.html', contexto)


@login_required
def EditarReceta(request, pk):
    receta = get_object_or_404(Receta, pk=pk)

    if request.method == 'POST':
        form = RecetaForm(request.POST, request.FILES, instance=receta)
        if form.is_valid():
            form.save()
            return redirect('recetas:detalle', pk=pk)
    else:
        form = RecetaForm(instance=receta)

    context = {
        'form': form,
    }
    return render(request, 'recetas/editar.html', {'form': form, 'receta': receta})
 