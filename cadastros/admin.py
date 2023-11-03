from django.contrib import admin

from cadastros.models import Cidade, Estado, Pais

# Register your models here.

class EstadoInline(admin.TabularInline):
    model = Estado

class PaisAdmin(admin.ModelAdmin):

    fields = ('nome', )
    inlines = [
        EstadoInline
    ]

admin.site.register(Cidade)
admin.site.register(Estado)
admin.site.register(Pais, PaisAdmin)