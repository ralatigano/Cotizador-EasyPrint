from django import forms
from Products.models import Producto, Categoria


class PresupuestoForm(forms.Form):
    cliente=forms.CharField(label='Cliente',max_length=100)
    cat = forms.ModelChoiceField(label='Categoría',queryset=Categoria.objects.all())
    prod = forms.ModelChoiceField(label='Producto',queryset=Producto.objects.filter(resultado=0))
    cantidad=forms.IntegerField(label='Cantidad',min_value=1)
    descuento=forms.IntegerField(label='Descuento',min_value=0)
    info_adic = forms.CharField(label='Información adicional',max_length=200, widget=forms.Textarea())
    
