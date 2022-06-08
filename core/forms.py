from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):

    #nombre = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    #correo = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    #tipo_consulta = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    #mensaje = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    
    class Meta:
        model = Contacto
        fields = ["nombre", "correo", "tipo_consulta", "mensaje", "avisos"]
        #fields = '__all__'