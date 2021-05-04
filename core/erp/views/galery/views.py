from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from core.erp.forms import PhotoForm
from core.erp.mixins import ValidatePermissionRequiredMixin
from django.core.exceptions import ValidationError
from django.contrib import messages
from core.erp.models import Photo,Category
from django.contrib.auth.decorators import  login_required


@login_required(login_url='/')
def eliminar(request, post_id):
    try:
        post = Photo.objects.get(pk=post_id)
    except Photo.DoesNotExist:
        messages.error(request, "NO EXISTE")
        return redirect('erp:galery_list')
    
    post.delete()
    messages.error(request, f"Se a eliminado la imagen correctamente!!")
    return redirect('erp:galery_list')



@login_required(login_url='/')
def gallery(request):
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)

    categories = Category.objects.all()
    context = {'categories': categories, 'photos': photos ,'title':'Galeria'}
    return render(request, 'Galery/list.html', context)

@login_required(login_url='/')
def addPhoto(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(
                name=data['category_new'])
        else:
            category = None

        for image in images:
            photo = Photo.objects.create(
                category=category,
                description=data['description'],
                image=image,
            )

        return redirect('erp:galery_list')

    context = {'categories': categories}
    return render(request, 'Galery/create.html', context)




#VALIDACIONES


def verificar(nro):
    l = len(nro)
    if l == 10 or l == 13: # verificar la longitud correcta
        cp = int(nro[0:2])
        if cp >= 1 and cp <= 22: # verificar codigo de provincia
            tercer_dig = int(nro[2])
            if tercer_dig >= 0 and tercer_dig < 6 : # numeros enter 0 y 6
                if l == 10:
                    return __validar_ced_ruc(nro,0)                       
                elif l == 13:
                    return __validar_ced_ruc(nro,0) and nro[10:13] != '000' # se verifica q los ultimos numeros no sean 000
            elif tercer_dig == 6:
                return __validar_ced_ruc(nro,1) # sociedades publicas
            elif tercer_dig == 9: # si es ruc
                return __validar_ced_ruc(nro,2) # sociedades privadas
            else:
                raise Exception(u'Tercer digito invalido') 
        else:
            raise Exception(u'Codigo de provincia incorrecto') 
    else:
        raise Exception(u'Longitud incorrecta del numero ingresado')
    
def __validar_ced_ruc(nro,tipo):
    total = 0
    if tipo == 0: # cedula y r.u.c persona natural
        base = 10
        d_ver = int(nro[9])# digito verificador
        multip = (2, 1, 2, 1, 2, 1, 2, 1, 2)
    elif tipo == 1: # r.u.c. publicos
        base = 11
        d_ver = int(nro[8])
        multip = (3, 2, 7, 6, 5, 4, 3, 2 )
    elif tipo == 2: # r.u.c. juridicos y extranjeros sin cedula
        base = 11
        d_ver = int(nro[9])
        multip = (4, 3, 2, 7, 6, 5, 4, 3, 2)
    for i in range(0,len(multip)):
        p = int(nro[i]) * multip[i]
        if tipo == 0:
            total+=p if p < 10 else int(str(p)[0])+int(str(p)[1])
        else:
            total+=p
    mod = total % base
    val = base - mod if mod != 0 else 0
    return val == d_ver

def vcedula(texto):
    # sin ceros a la izquierda
    nocero = texto.strip("0")
    
    cedula = int(nocero,0)
    verificador = cedula%10
    numero = cedula//10
    
    # mientras tenga números
    suma = 0
    while (numero > 0):
        
        # posición impar
        posimpar = numero%10
        numero   = numero//10
        posimpar = 2*posimpar
        if (posimpar  > 9):
            posimpar = posimpar-9
        
        # posición par
        pospar = numero%10
        numero = numero//10
        
        suma = suma + posimpar + pospar
    
    decenasup = suma//10 + 1
    calculado = decenasup*10 - suma
    if (calculado  >= 10):
        calculado = calculado - 10

    if (calculado == verificador):
        validado = 1
    else:
        validado = 0
        
    return (validado)