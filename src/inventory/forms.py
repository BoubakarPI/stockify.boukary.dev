from django.forms import ModelForm

from .models import  Commande

from django import forms
from .models import Commande

class CommandeForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = ['produit', 'quantite', 'statut']

    def __init__(self, *args, **kwargs):
        super(CommandeForm, self).__init__(*args, **kwargs)
        self.fields['produit'].widget.attrs['readonly'] = True  # Lecture seule
 # Statut peut être modifiable à ce moment, sinon on pourrait le laisser en lecture seule.



