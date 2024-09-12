from django.contrib import admin
from .models import Categoria
from .models import Producto
from .models import Cliente #modelo cliente

#modificaciones del código tarea con grappelli
def incrementar_stock(modeladmin, request, queryset):
    for producto in queryset:
        producto.stock += 1
        producto.save()
incrementar_stock.short_description = 'Incrementar stock en 1'
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'stock')
    search_fields = ['nombre']
    actions = [incrementar_stock]

#modificaciones del código tarea con grappelli
# 
#     
admin.site.register(Categoria)# Register your models here.
admin.site.register(Producto)
admin.site.register(Cliente) #modelo cliente