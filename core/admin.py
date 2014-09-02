from django.contrib import admin

from .models import Noticia, Site


class NoticiaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Noticia, NoticiaAdmin)


class SiteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'site', 'start', 'tipo', 'status')
    list_filter = ('tipo', 'status')
    list_editable = ('status',)
    search_fields = ('nome', 'site')


admin.site.register(Site, SiteAdmin)
