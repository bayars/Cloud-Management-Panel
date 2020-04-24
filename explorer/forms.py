from django import forms
from .models import Servers


class AddServer(forms.ModelForm):
    class Meta:
        model = Servers
        fields = ['boxname','ip','port','username','password','path']
        
class RemServer(forms.Form):
    boxname = forms.ModelChoiceField(queryset=Servers.objects.all()) 