from django.urls import path
from categoria_app import views 

urlpatterns = [
    path('categorias',views.inicio_vistaCategorias, name="categorias"),
    path("registrarCategorias/",views.registrarCategorias,name="registrarCategorias"),
    path("seleccionarCategorias/<id_categoria>",views.seleccionarCategorias,name="seleccionarCategorias"),
    path("editarCategorias/",views.editarCategorias,name="editarcategorias"),
    path("borrarCategorias/<id_categoria>",views.borrarCategorias,name="borrarCategorias"),
]