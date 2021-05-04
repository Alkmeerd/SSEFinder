from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username', 'chp_staff_no', 'email_ad','first_name', 'last_name',)
    list_filter = ('username', 'chp_staff_no', 'email_ad', 'first_name', 'last_name')
    fieldsets = (
        (None, {'fields': ('username', 'password', 'chp_staff_no', 'email_ad', 'first_name', 'last_name')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'chp_staff_no', 'email_ad' , 'first_name', 'last_name')}
        ),
    )
    search_fields = ('username',)
    ordering = ('username',)

admin.site.register(Case)
admin.site.register(Event)
admin.site.register(CustomUser, CustomUserAdmin)