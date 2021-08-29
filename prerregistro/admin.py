from django.contrib import admin
from prerregistro.models import Prerregistro

# Register your models here.
@admin.register(Prerregistro)
class PrerregistroAdmin(admin.ModelAdmin):
    exclude = ('usuario_db',)
