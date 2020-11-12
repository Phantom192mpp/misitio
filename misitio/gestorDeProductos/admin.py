from django.contrib import admin
from .models import Producto
from .models import Marca
from .models import Sucursal
from .models import Categoria
from .models import Cliente
from .models import Boleta
from .models import Detalle_Boleta
# Register your models here.

class AdminProducto(admin.ModelAdmin):
    list_display = ['codigo', 'descripcion', 'stock']
    list_filter  = ['descripcion']
    search_fields = ['codigo', 'descripcion']
    list_display_links = ['descripcion']
    ordering     = ['descripcion']

admin.site.register(Producto, AdminProducto)
admin.site.register(Marca)
admin.site.register(Sucursal)
admin.site.register(Categoria)
admin.site.register(Cliente)
admin.site.register(Boleta)
admin.site.register(Detalle_Boleta)
