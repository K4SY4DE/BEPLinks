from django.contrib import admin
from .models import Tema, Recurso
# Register your models here.

@admin.register(Tema)
class TemaAdmin(admin.ModelAdmin):
    list_display = ('titulo',)


@admin.register(Recurso)
class RecursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tema', 'tipo', 'gratuito', 'prestigio')
    list_filter = ('tema', 'gratuito', 'tipo')
    search_fields = ('nome',)