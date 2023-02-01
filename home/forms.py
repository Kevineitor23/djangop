from django.forms import ModelForm,forms
from home.models import Reclutador

class ReclutadorForms(ModelForm):
    class Meta:
        fields = ('__all__')
        model = Reclutador 
      
    