from django.forms import ModelForm

from .models import  Commande

class CommandeForm(ModelForm):
    class Meta:
        model = Commande
        fields = '__all__'  # Statut peut être modifiable à ce moment, sinon on pourrait le laisser en lecture seule.



