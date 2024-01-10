from django.urls import path
from . import views


app_name = 'recetas'

urlpatterns = [
    path('', views.ListarRecetas, name='listar'),
    path('detalle/<int:pk>', views.DetalleReceta, name='detalle'),
    path('addReceta', views.AddReceta, name='addreceta'),
    path('comentario/add/<int:receta_id>', views.AddComentario, name='add_comentario'),
]
