from django.contrib import admin
from .models import Atencion, Comentarios, Empleado, Encuestas, Georeferencia, Gestion, Ingrediente, Ofertas, Orden, OrdenPlatillo, Platillo, PlatilloIngrediente, PlatilloTipoPlatillo, Recibo, Registro, Reservacion, Sucursal, TipoPlatillo, Usuario, Administrador

# Class of models

class AdministradorAdmin(admin.ModelAdmin):
    list_display=("nombre","usuario")
    search_fields=("nombre","usuario")

class AtencionAdmin(admin.ModelAdmin):
    list_display=("apertura","clausura")

class ComentarioAdmin(admin.ModelAdmin):
    list_display=("comentario","usuario_ci")

class EmpleadoAdmin(admin.ModelAdmin):
    list_display=("nombre","rol")
    search_fields=("ci","nombre","rol")

class EncuestaAdmin(admin.ModelAdmin):
    list_display=("calidad","empleados","recervacion","delivery")

class GeoreferenciaAdmin(admin.ModelAdmin):
    search_fields=("telefono","nit")

class GestionAdmin(admin.ModelAdmin):
    list_display=("fecha")
    search_fields=("sucursal_su")
    list_filter=("fecha")

class OfetasAdmin(admin.ModelAdmin):
    list_display=("descuento","descripcion")

class PlatilloAdmin(admin.ModelAdmin):
    list_display=("nombre","descripcion")


class ReservacionAdmin(admin.ModelAdmin):
    list_display=("fecha","mensaje")
    search_fields=("nombre","usuario_ci")

class UsuarioAdmin(admin.ModelAdmin):
    list_display=("ci","nombre","correo")
    search_fields=("ci","nombre")



# Register your models here.

admin.site.register(Administrador, AdministradorAdmin)
admin.site.register(Atencion, AtencionAdmin)
admin.site.register(Comentarios, ComentarioAdmin)
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Encuestas, EncuestaAdmin)
admin.site.register(Georeferencia, GeoreferenciaAdmin)
admin.site.register(Gestion, GeoreferenciaAdmin)
admin.site.register(Ingrediente)
admin.site.register(Ofertas, OfetasAdmin)
admin.site.register(Orden)
admin.site.register(OrdenPlatillo)
admin.site.register(Platillo, PlatilloAdmin)
admin.site.register(PlatilloIngrediente)
admin.site.register(PlatilloTipoPlatillo)
admin.site.register(Recibo)
admin.site.register(Registro)
admin.site.register(Reservacion, ReservacionAdmin)
admin.site.register(Sucursal)
admin.site.register(TipoPlatillo)
admin.site.register(Usuario, UsuarioAdmin)