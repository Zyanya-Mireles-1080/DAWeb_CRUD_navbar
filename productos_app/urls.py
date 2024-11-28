from django.urls import path
from productos_app import views 

urlpatterns = [
    path('productos',views.inicio_vistaProductos, name="productos"),
    path("registrarProductos/",views.registrarProductos,name="registrarProductos"),
    path("seleccionarProductos/<id_producto>",views.seleccionarProductos,name="seleccionarProductos"),
    path("editarProductos/",views.editarProductos,name="editarProductos"),
    path("borrarProductos/<id_producto>",views.borrarProductos,name="borrarProductos"),
]