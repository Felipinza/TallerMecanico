from django import forms
from prueba.models import Imagen
class ImageForm(forms.ModelForm):
   class Meta:
      model = Imagen
      fields = ['idImagen','texto','nombre','fechaRegistro','categoria','mecanico','archivo']