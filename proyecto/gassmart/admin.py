from django.contrib import admin

from .models import Empresa
from .models import Usuario
from .models import Consumo
from .models import Balones

admin.site.register(Empresa)
admin.site.register(Usuario)
admin.site.register(Consumo)
admin.site.register(Balones)