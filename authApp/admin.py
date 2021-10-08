from django.contrib import admin
from .models.user import User
from .models.paciente import Paciente
from .models.historia import Historia
from .models.cita import Cita

admin.site.register(User)
admin.site.register(Paciente)
admin.site.register(Historia)
admin.site.register(Cita)

# Register your models here.
