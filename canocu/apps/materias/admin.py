from django.contrib import admin

from .models import Categoria, Materias, Assistant, Comments, Semestre, Carrera

admin.site.register(Materias)
admin.site.register(Categoria)
admin.site.register(Assistant)
admin.site.register(Semestre)
admin.site.register(Carrera)
admin.site.register(Comments)