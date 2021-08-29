from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UsuarioCreationForm, UsuarioChangeForm
from .models import Usuario
from django.utils.translation  import ugettext_lazy as _

class UsuarioAdmin(UserAdmin):
    add_form = UsuarioCreationForm
    form = UsuarioChangeForm
    model = Usuario
    list_display = [ 'username', 'email', 'es_admin', 'is_staff']
    
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Perfil'), {'fields': ('es_admin',)}),
    )

admin.site.register(Usuario, UsuarioAdmin)