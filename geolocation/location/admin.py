from django.contrib import admin
from . models import Ubicacion
from . models import Delito

# Register your models here.

admin.site.register(Ubicacion)
admin.site.register(Delito)