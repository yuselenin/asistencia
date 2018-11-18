from django import forms
from django.contrib import admin
# admins
from django.contrib.auth.admin import UserAdmin
# forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from django.contrib.auth.models import User as UserOld
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext_lazy as _

# models
from .models import Usuario


class UsuarioCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Usuario  # get_user_model()


class UsuarioChangeForm(UserChangeForm):
    description = forms.CharField(
        label=_('Description'), required=False, initial='edit',
        widget=forms.Textarea)

    # is_staff = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

    class Meta(UserChangeForm.Meta):
        model = Usuario  # get_user_model()


class UsuarioAdmin(UserAdmin):
    form = UsuarioChangeForm
    add_form = UsuarioCreationForm

    # list_display = ('username', 'email',
    #                'first_name', 'last_name', 'is_staff', 'status')

    # list_filter = ('is_staff', 'is_superuser',
    #               'is_active', 'groups', 'date_joined')

    # date_hierarchy = 'date_joined'

    raw_id_fields = ('persona',)


admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(ContentType)
admin.site.register(Permission)
