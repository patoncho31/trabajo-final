from django.urls import path
from . import views


app_name = 'recetas'

urlpatterns = [
    path('', views.ListarRecetas, name='listar'),
    path('detalle/<int:pk>', views.DetalleReceta, name='detalle'),
    path('addReceta', views.AddReceta, name='addreceta'),
    path('recetas/<int:pk>/edit/', views.EditarReceta, name='edit_receta'),
    
    #url de Comentario
    path('comentario/add/<int:receta_id>', views.AddComentario, name='add_comentario'),
    path('comentario/delete/<int:comentario_id>', views.BorrarComentario, name='delete_comentario'),
    path('comentario/edit/<int:comentario_id>', views.EditarComentario, name='edit_comentario'),

]
