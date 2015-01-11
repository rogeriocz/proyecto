from django.contrib import admin
from . import models
#from django_markdown.admin import MarkdownModelAdmin

class EntryAdmin(admin.ModelAdmin):
	list_display = ("titulo", "creado")
	prepopulated_fields = {"slug": ("titulo",)}

admin.site.register(models.Entrada, EntryAdmin)

# Register your models here.
