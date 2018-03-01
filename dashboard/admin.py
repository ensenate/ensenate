from django.contrib import admin
#from .models import Unidad
# Register your models here.
#
from .models import Unidad, Leccion, Palabra#Category, Item


class Palabraline(admin.TabularInline):
	model = Palabra
	extra = 1

class LeccionAdmin(admin.ModelAdmin):
	inlines = [Palabraline,]

#class UnidadAdmin(admin.ModelAdmin):
#	inlines = [ ]

admin.site.register(Unidad)
admin.site.register(Leccion, LeccionAdmin)
admin.site.register(Palabra)
