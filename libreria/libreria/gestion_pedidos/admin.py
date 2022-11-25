from django.contrib import admin

from gestion_pedidos.models import Items, Clientes, Pedido


class ItemsAdmin(admin.ModelAdmin):
    list_display = ("nombre","price","seccion")
    search_fields = ("nombre", "seccion")
    list_filter = ("seccion",)

class ClientesAdm(admin.ModelAdmin):
    list_display= ("nombre","email")

class PedidoAdm(admin.ModelAdmin):
    list_display = ("num_pedido", "fecha", "entregado")
    list_filter= ("fecha", "entregado")
    

# Register your models here.
admin.site.register(Items, ItemsAdmin)
admin.site.register(Clientes,ClientesAdm)
admin.site.register(Pedido, PedidoAdm)