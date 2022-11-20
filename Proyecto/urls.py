from django.contrib import admin
from django.urls import path
from Datos import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.principal, name="principal"),
    path("registro/",views.registro, name="registro"),
    path("tareas/",views.tareas, name="tareas"),
    path("tareascompletadas/",views.tareascompletadas, name="tareascompletadas"),
    path("tareas/crear",views.creartareas, name="creartareas"),
    path("tareasdetalle/<id>",views.tareasdetalle, name='tareasdetalle'),
    path("tareas/<id>/completar",views.completartareas, name='completartareas'),
    path("tareas/<id>/eliminar",views.eliminartareas, name='eliminartareas'),
    path("salir/",views.salir, name="salir"),
    path("ingresar/",views.ingresar, name="ingresar"),
     
]
