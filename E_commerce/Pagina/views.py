from django.shortcuts import render, HttpResponse

from django.template import Template, Context
from django.template.loader import get_template
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect
from django.db.models import Sum
# Create your views here.

from .models import Administrador
from .models import Reservacion
from .models import Usuario
from .models import OrdenPlatillo
from .models import Sucursal
from .models import Encuestas

def home(request):
    Cliente = Usuario.objects.all()
    CountCliente = Cliente.count()
    Reserv = Reservacion.objects.all()
    CountReserv = Reserv.count()
    Platillos = OrdenPlatillo.objects.all()
    CountPlatillos = Platillos.count()
    Sucur = Sucursal.objects.all()
    CountSucur = Sucur.count()
    context = {
        'CountCliente': CountCliente,
        'CountReserv': CountReserv,
        'CountPlatillos': CountPlatillos,
        'CountSucur': CountSucur
    }

    if request.method=='POST':
        nombreUsuario=request.POST['userName']
        Email=request.POST['userEmail']
        Fecha=request.POST['reservationDate']
        Cantidad=request.POST['totalPeople']
        Comentario=request.POST['userMessage']
        Costo=20
        Reservacion(fecha=Fecha,costo=Costo,personas=Cantidad,mensaje=Comentario,nombre=nombreUsuario,correo=Email).save()
        messages.success(request, 'La reservacion del cliente '+request.POST['userName']+' Ya a sido registrado.')
        return render(request, 'home.html', context)
    else:
        return render(request, 'home.html', context)

    
def blog(request):

    return render(request, 'blog.html')
    
def blogLeft(request):

    return render(request, 'blog-left.html')

def nosotros(request):

    return render(request, 'nosotross.html')

def login(request):
    if request.method=='POST':
        try:
            detalleUsuario=Administrador.objects.get(usuario=request.POST['user'], contrasenia=request.POST['pass'])
            request.session['usuario']=detalleUsuario.usuario
            return redirect('admin/Pagina')
        except Administrador.DoesNotExist as e:
            messages.success(request, 'Nombre de usuario o Password no es correcto..!')
    return render(request, 'login.html')

