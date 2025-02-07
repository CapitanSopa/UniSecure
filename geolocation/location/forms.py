from django import forms
from .models import Ubicacion
from .models import Delito

class UbicacionForm(forms.ModelForm):

    class Meta:

        model = Ubicacion
        fields = ('codigo_postal',
                  'nombre_ciudad',
                  'nombre_colonia',
                  'seguridad_zona',)
        
class DelitoForm (forms.ModelForm):

    class Meta:

        model = Delito

        fields = ['codigop_delito', 'delegacion_delito', 'calle_delito', 'colonia_delito', 'tipo_delito', 'descripcion']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }
