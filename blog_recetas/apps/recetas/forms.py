# forms.py en tu aplicación

from django import forms
from .models import Receta,Comentario

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['titulo',
                  'descripcion',
                  'ingredientes',
                  'instrucciones',
                  'categoria',
                  'imagen']

    ##widgets = {
     ##   'descripcion': forms.Textarea(attrs={'rows': 3}),
     ##   'ingredientes': forms.Textarea(attrs={'rows': 5}),
     #   'instrucciones': forms.Textarea(attrs={'rows': 10}),
   ## }
   
      
class ComentarioForm(forms.ModelForm):
   
    class Meta:
        model = Comentario
        fields = [
            'contenido',
        ]
        exclude = ['usuario']
   
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)


        super(ComentarioForm, self).__init__(*args, **kwargs)
        if user:
            self.instance.usuario = user.username 