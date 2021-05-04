
from django.views.generic import TemplateView


from django.shortcuts import render, redirect 

import json
import os
from django.http import HttpResponse

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponseRedirect

from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, View
from django.conf import settings
from xhtml2pdf import pisa
from django.template.loader import get_template

from core.erp.forms import MusicForm, LiveForm
from core.erp.mixins import ValidatePermissionRequiredMixin
from core.erp.models import Music, Live
from core.erp.models import Photo,Category
from core.erp.models import Advertising


# Create your views here.
class IndexView(ListView):
    model = Advertising
    template_name = 'home/body.html'
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []               
                for i in Advertising.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado Publicidad'
        context['create_url'] = reverse_lazy('erp:advertising_create')
        context['list_url'] = reverse_lazy('erp:advertising_list')
        context['entity'] = 'Publicidad'
        context['var'] = self.get_queryset()
        return context




class AboutView(TemplateView):
    template_name = 'home/about.html'




class RadioOnlineView(TemplateView):
    template_name = 'home/radioOnline.html'

class MusicaView(ListView):
    model = Music
    template_name = "home/musica.html"
    #permission_required = 'view_music'
    @method_decorator(csrf_exempt)
    #@method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                position = 1
                for i in Music.objects.all():
                    item = i.toJSON()
                    item['position'] = position
                    data.append(item)
                    position += 1
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)        
        return JsonResponse(data,safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Listado de Curso'
        context['create_url'] = reverse_lazy('erp:curso_create')
        context['list_url'] = reverse_lazy('erp:curso_list')
        context['entity'] = 'Curso'
        context['curso'] = self.get_queryset()   #agregamos la consulta al contexto
        #context['silabo'] = self.get_queryset()#context['form'] = self.form_class
        return context
    

class RadioView(ListView):
    model = Live
    template_name = "home/radio.html"
    #permission_required = 'view_music'
    @method_decorator(csrf_exempt)
    #@method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                position = 1
                for i in Music.objects.all():
                    item = i.toJSON()
                    item['position'] = position
                    data.append(item)
                    position += 1
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)        
        return JsonResponse(data,safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Listado de Curso'
        context['create_url'] = reverse_lazy('erp:curso_create')
        context['list_url'] = reverse_lazy('erp:curso_list')
        context['entity'] = 'Curso'
        context['curso'] = self.get_queryset()   #agregamos la consulta al contexto
        #context['silabo'] = self.get_queryset()#context['form'] = self.form_class
        return context

def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'home/imagenview.html', {'photo': photo})


def gallery(request):
    category = request.GET.get('category')
   
    
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)

    categories = Category.objects.all()
    context = {'categories': categories, 'photos': photos}
    return render(request, 'home/galery.html', context)


class AdvertisingListView(LoginRequiredMixin, ListView):
    model = Advertising
    template_name = 'home/body.html'
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []               
                for i in Advertising.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado Publicidad'
        context['create_url'] = reverse_lazy('erp:advertising_create')
        context['list_url'] = reverse_lazy('erp:advertising_list')
        context['entity'] = 'Publicidad'
        context['var'] = self.get_queryset()
        return context

