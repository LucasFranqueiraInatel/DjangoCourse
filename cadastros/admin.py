from django.contrib import admin

from cadastros.models import Cidade, Estado, Pais

# Register your models here.

admin.site.register(Cidade)
admin.site.register(Estado)
admin.site.register(Pais)