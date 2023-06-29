from django.urls import path
from . import views #el punto quiere decir que importamos desde el mismo paquete

urlpatterns = [
    path("", views.index, name="index") #en esta ruta se llama la función index creada en el modulo views, 
]                                       #se le asigna un nombre "index" y se deja la ruta vacia "" ya que esta dentro del mismo paquete