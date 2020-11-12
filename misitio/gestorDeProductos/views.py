from django.shortcuts import render
from gestorDeProductos.models import Sucursal, Marca, Categoria, Producto
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import logout as do_logout
# Create your views here.


    
def index(request):
    return render(request, 'index.html', {})

def galeria(request):
    if request.user.is_authenticated:
        return render(request, "galeria.html")
    return redirect('/login')
def registro(request):
    return render(request, "registro.html")

    
def login(request):
    return render(request, 'Login.html', {})

def contactanos(request):
    return render(request, 'cotactanos.html', {})

def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('index')
    
def sucursal(request):
    mensaje  = ""
    listado  = {}
    item     = {}
    if request.method == "POST":

        if 'btnGuardar' in request.POST:
            id          =int("0" + request.POST["txtId"])
            nombre      =request.POST["txtNombre"]
            direccion   =request.POST["txtDireccion"]
            telefono    =request.POST["txtTelefono"]
            encargado   =request.POST["txtEncargado"]
            
        if 'btnGuardar' in request.POST:
            if id < 1:
                Sucursal.objects.create(nombre = nombre, direccion = direccion, telefono = telefono, encargado = encargado)
            else:
                item 			= Sucursal.objects.get(pk = id)
                item.nombre 	= nombre
                item.direccion 	= direccion
                item.telefono 	= telefono
                item.encargado 	= encargado
                item.save()
                item = {}
            
            mensaje      = "Operacion exitosa."

        elif 'btnListar' in request.POST:
            listado = Sucursal.objects.all()
            #listado = Sucursal.objects.filter(nombre__contains = nombre, 
			#									encargado__contains = encargado)
		    
        
        elif 'btnBuscar' in request.POST:
            id   = request.POST['txtId']
            item = Sucursal.objects.get(pk = id)


    contexto     = {'mensaje' : mensaje, 'listado' : listado, 'item' : item}

    return render(request, 'sucursal.html', contexto)     


def producto(request):
    mensaje = ""
    listado = {}
    item = {}
    marca = {}
    categoria = {}
    marca = Marca.objects.filter(activo = True)
    categoria = Categoria.objects.filter(activo = True)

    if request.method == "POST":
        id 			= int("0" + request.POST['txtId'])
        idMarca		= int(request.POST['cmbMarca'])
        idCategoria	= int(request.POST['cmbCategoria'])
        codigo		= int("0" + request.POST['txtCodigo'])
        descripcion	= request.POST['txtDescripcion']
        stock		= int("0" + request.POST['txtStock'])
        precioCosto	= int("0" + request.POST['txtPrecioCosto'])
        precioVenta = int("0" + request.POST['txtPrecioVenta'])

        if 'btnGuardar' in request.POST:
           # if id < 1:
                idMarca 	= Marca.objects.get(pk=idMarca)
                idCategoria = Categoria.objects.get(pk=idCategoria)
                Producto.objects.create(codigo=codigo, descripcion=descripcion,stock=stock, precioCosto=precioCosto,precioVenta=precioVenta, marca=idMarca,categoria=idCategoria)
            #else:
             #   item 		    	= Producto.objects.get(pk = id)
              #  item 		    	= Producto.objects.get(pk = idMarca)
               # item 		    	= Producto.objects.get(pk = idCategoria)
                #item.codigo 	    = codigo
               # item.descripcion 	= descripcion
               # item.stock  	    = stock
                #item.precioCosto 	= precioCosto
               # item.precioVenta 	= precioVenta
              #  item.save()
             #   item = {}
        elif 'btnListar' in  request.POST:
            listado = Producto.objects.all()
       # elif 'btnBuscar' in request.POST:
        #    codigo 	= int("0" + request.POST['txtCodigo'])
         #   item = Producto.objects.get(pk = codigo)
    contexto = {'mensaje' : mensaje, 'listado': listado, 'item': item, 'marca':marca, 'categoria':categoria }
    return render(request, 'producto.html', contexto)
    
    
def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('galeria')    
    # Si llegamos al final renderizamos el formulario
    return render(request, "Login.html", {'form': form})
    
    
def registro(request):
    # Creamos el formulario de autenticación vacío
    form = UserCreationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = UserCreationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():

            # Creamos la nueva cuenta de usuario
            user = form.save()

            # Si el usuario se crea correctamente 
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('login')
    
    form.fields['username'].help_text = None
    form.fields['password1'].help_text = None
    form.fields['password2'].help_text = None
    
    # Si llegamos al final renderizamos el formulario
    return render(request, "registro.html", {'form': form})
  