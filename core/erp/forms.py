from datetime import datetime

from django import forms
from django.forms import ModelForm

from core.erp.models import Music, Live, Photo , Category,Advertising




class MusicForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #     form.field.widget.attrs['class'] = 'form-control'
        #     form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['title'].widget.attrs['autofocus'] = True

    class Meta:
        model = Music
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese el Titulo de la canción',
                }
            ),
            
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class LiveForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #     form.field.widget.attrs['class'] = 'form-control'
        #     form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['title'].widget.attrs['autofocus'] = True

    class Meta:
        model = Live
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese el Titulo del Live',
                }
            ),
            'link': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese el artista',
                }
            ),
            'usuario': forms.Select(
                attrs={
                    'class': 'select2',
                    'style': 'width: 100%'
                }
            ),
            
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class PhotoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #     form.field.widget.attrs['class'] = 'form-control'
        #     form.field.widget.attrs['autocomplete'] = 'off'
        #self.fields['title'].widget.attrs['autofocus'] = True

    class Meta:
        model = Photo
        fields = '__all__'
        widgets = {
            'category': forms.Select(
                attrs={
                    'class': 'select2',
                    'style': 'width: 100%'
                }
            ),
            'image': forms.FileInput(
                attrs={
                    'placeholder': 'Imagen',
                    'name': 'images',
                    'class': 'form-control-file'
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese el artista',
                }
            ),
            
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class CategoryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #     form.field.widget.attrs['class'] = 'form-control'
        #     form.field.widget.attrs['autocomplete'] = 'off'
        #self.fields['title'].widget.attrs['autofocus'] = True

    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese el Nombre de la categoria:',
                }
            ),
            
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class AdvertisingForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #     form.field.widget.attrs['class'] = 'form-control'
        #     form.field.widget.attrs['autocomplete'] = 'off'
        #self.fields['title'].widget.attrs['autofocus'] = True

    class Meta:
        model = Advertising
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese el Nombre de la empresa:',
                }
            ),
            'descripcion': forms.Textarea(
                attrs={
                    'placeholder': 'Ingrese la descripcion de la empresa:',
                }
            ),
            'link': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese el Link de la empresa:',
                }
            ),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
