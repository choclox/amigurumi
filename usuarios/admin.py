from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario  # Importas el modelo

class UsuarioAdmin(UserAdmin):
    # Definir cómo se muestra el modelo en el admin
    list_display = ('username', 'email', 'first_name', 'last_name', 'es_vendedor')
    list_filter = ('es_vendedor',)
    search_fields = ('username', 'email')

    fieldsets = UserAdmin.fieldsets + (
        ('Rol de usuario', {'fields': ('es_vendedor',)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Rol de usuario', {'fields': ('es_vendedor',)}),
    )
# Registrar el modelo
admin.site.register(Usuario, UsuarioAdmin)
