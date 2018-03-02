from django.contrib import admin
#from .models import Unidad
# Register your models here.
#
from .models import DatosUnidadUsuario
from .models import DatosLeccionUsuario
from .models import User

admin.site.register(DatosUnidadUsuario)

admin.site.register(DatosLeccionUsuario)

admin.site.register(User)