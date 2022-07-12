from django.shortcuts import render, redirect, get_object_or_404

from .forms import ContactoForm, ProductoForm, CustomUserCreationForm, MascotaForm
from .models import Producto, Mascota
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login 
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework import viewsets, generics
from .serializers import ProductoSerializer, MascotaSerializer


# Create your views here.


class ProductoViewset(viewsets.ModelViewSet):

    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def get_queryset(self):
        productos = Producto.objects.all()

        nombre = self.request.GET.get('nombre')

        if nombre:
            productos = productos.filter(nombre__contains=nombre)
        
        return productos


class MascotaViewset(viewsets.ModelViewSet):

    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer

    def get_queryset(self):
        mascotas = Mascota.objects.all()

        nombre = self.request.GET.get('especie')

        if nombre:
            mascotas = mascotas.filter(nombre__contains=especie)
        
        return mascotas


## TODOS LOS HTML RELACIONADOS A LAS PESTAÑAS EXISTENTES

def home(request):
    return render(request, 'app/home.html')



def productos(request):
    return render(request, 'app/productos.html')



def contacto(request):
    data = {
        'form': ContactoForm()  
    }

    if request.method == 'POST':
        formulario = ContactoForm (data=request.POST)
        if formulario.is_valid():
            formulario.save()
        
        else:
            data["form"] = formulario

    return render(request, 'app/contacto.html', data)




def comentarios(request):
    return render(request, 'app/comentarios.html')




def blog(request):
    return render(request, 'app/blog.html')



## TODOS LOS HTML RELACIONADOS AL CRUD DEL PRODUCTO


@permission_required('app.add_producto')
def agregar_producto(request):

    data = {
        'form': ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "guardado correctamente"
        
        else:
            data["form"] = formulario

    return render(request, 'app/producto/agregar.html', data)



def listar_productos(request):

    productos = Producto.objects.all()

    data = {
        'productos': productos
    }
    
    return render(request, 'app/producto/listar.html', data)


@permission_required('app.change_producto')
def modificar_producto(request, id):

    producto = get_object_or_404(Producto, id=id)

    data = {
        'form': ProductoForm(instance = producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto)
        
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_productos")
        data["form"] = formulario 

    return render(request, 'app/producto/modificar.html', data)

@permission_required('app.delete_producto')
def eliminar_producto(request, id):

    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect(to="listar_productos")



# TODOS LOS HTML RELACIONADOS AL CRUD DE MASCOTA

@permission_required('app.add_mascota')
def agregar_mascota(request):

    data = {
        'forms': MascotaForm()
    }

    if request.method == 'POST':
        formulario = MascotaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "guardado correctamente"
        
        else:
            data["forms"] = formulario

    return render(request, 'app/mascota/agregar.html', data)


def listar_mascota(request):

    mascota = Mascota.objects.all()

    data = {
        'mascota': mascota
    }
    
    return render(request, 'app/mascota/listar.html', data)

@permission_required('app.change_mascota')
def modificar_mascota(request, id):

    mascota = get_object_or_404(Mascota, id=id)

    data = {
        'forms': MascotaForm(instance = mascota)
    }

    if request.method == 'POST':
        formulario = MascotaForm(data=request.POST, instance=mascota)
        
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_mascota")
        data["forms"] = formulario 

    return render(request, 'app/mascota/modificar.html', data)

@permission_required('app.delete_producto')
def eliminar_mascota(request, id):

    producto = get_object_or_404(Mascota, id=id)
    producto.delete()
    return redirect(to="listar_mascota")










def registro(request):

    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data= request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect(to="home")
        data["form"] = formulario
        
    return render(request, 'registration/registro.html', data)
