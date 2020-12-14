from django.contrib import admin

from .models import I_Beam, Standart

class BeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'h', 'b', 'P', 'standart')
    list_display_links = ('id', 'title')
    list_per_page = 25

class StandartAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    list_per_page = 25

admin.site.register(I_Beam, BeamAdmin)
admin.site.register(Standart, StandartAdmin)