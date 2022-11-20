from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.db import IntegrityError
from .forms import FormularioTareas
from .models import Tareas
from django.utils import timezone
from django.contrib.auth.decorators import login_required



# Create your views here.

def principal(request):
    return render(request,"Principal.html")

def registro(request):
    
    if request.method == "GET":
        return render(request, "Registro.html",{
            "form":UserCreationForm
        })
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                #registro usuario
                user= User.objects.create_user(username=request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect("tareas")
            except IntegrityError:
                return render(request, "Registro.html",{
                    "form":UserCreationForm,
                    "error": "El Usuario Ya Existe"
                }) 
        return render(request, "Registro.html",{
                    "form":UserCreationForm,
                    "error": "Las Contraseñas No Coinciden"
                })
        
@login_required
def tareas(request):
    tareas=Tareas.objects.filter(usuario=request.user, completado__isnull=True)
    return render(request, "Tareas.html",{'tareas':tareas})

@login_required
def tareascompletadas(request):
    tareas=Tareas.objects.filter(usuario=request.user, completado__isnull=False).order_by ("-completado")
    return render(request, "Tareas.html",{'tareas':tareas})
    
@login_required
def creartareas(request):
    
    if request.method == "GET":
        return render(request, "Crear_Tareas.html",{
            "form": FormularioTareas
        })
    else:
        try:
            form=FormularioTareas(request.POST)
            nueva_tarea=form.save(commit=False)
            nueva_tarea.usuario=request.user
            nueva_tarea.save()
            return redirect("tareas")
        except ValueError:
            return render(request, "Crear_Tareas.html",{
            "form": FormularioTareas,
            "error": "Ingrese Datos Validos"
        })
 
@login_required
def tareasdetalle(request, id):
    if request.method=="GET":
        tareas=Tareas.objects.get(id=id, usuario=request.user)
        form=FormularioTareas(instance=tareas)
        return render(request, "Tareas_Detalle.html", {"tareas":tareas, "form":form})
    else:
        try:
            tareas=Tareas.objects.get(id=id, usuario=request.user)
            form=FormularioTareas(request.POST, instance=tareas)
            form.save()
            return redirect("tareas")
        except ValueError:
            return render(request, "Tareas_Detalle.html", {"tareas":tareas, "form":form, "error":"Error Actualizando Tareas"})

@login_required           
def completartareas(request,id):   
     tareas=Tareas.objects.get(id=id, usuario=request.user)
     if request.method=="POST":
         tareas.completado=timezone.now()
         tareas.save()
         return redirect("tareas")
     
@login_required
def eliminartareas(request,id):   
     tareas=Tareas.objects.get(id=id, usuario=request.user)
     if request.method=="POST":
         tareas.delete()
         
         return redirect("tareas")

@login_required
def salir(request):
    logout(request)
    return redirect("principal")

def ingresar(request):
    if request.method == "GET":
        return render(request, "Ingreso.html",{
        "form": AuthenticationForm
        } )
    else:
        user=authenticate(
            request, username=request.POST["username"], password=request.POST
            ["password"])
        if user is None:
            return render(request, "Ingreso.html",{
                "form": AuthenticationForm,
                "error":"Usuario O Contraseña Incorrecta"
            } )
        else:
            login(request, user)
            return redirect("tareas")
        
        
        
        
    
    
    
    