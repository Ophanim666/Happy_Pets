from django.urls import path, include 
from .views import home, productos, contacto, comentarios, blog, agregar_producto, listar_productos, modificar_producto, eliminar_producto, registro, ProductoViewset, agregar_mascota, listar_mascota, modificar_mascota, eliminar_mascota, MascotaViewset
from rest_framework import routers

### ACUERDATE DE GUARDAR AQUI, EL PROGRAMA NO ESTA AVISANDO CUANDO NO GUARDAS AQUI Y ESTO NO PERMITE QUE SE EJECUTEN LOS VIEWS.


router = routers.DefaultRouter()
router.register('producto', ProductoViewset)
router.register('mascota', MascotaViewset)


urlpatterns = [
    path('', home, name="home"),
    path('productos/', productos, name="productos"),
    path('contacto/', contacto, name="contacto"),
    path('comentarios/', comentarios, name="comentarios"),
    path('blog/', blog, name="blog"),
    path('agregar-producto/', agregar_producto, name="agregar_producto"),
    path('agregar-mascota/', agregar_mascota, name="agregar_mascota"),
    path('listar-productos/', listar_productos, name="listar_productos"),
    path('listar-mascota/', listar_mascota, name="listar_mascota"),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_productos"),
    path('modificar-mascota/<id>/', modificar_mascota, name="modificar_mascota"),
    path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"),
    path('eliminar-mascota/<id>/', eliminar_mascota, name="eliminar_mascota"),
    path('registro/', registro, name="registro"),
    path('api/', include(router.urls)),




]