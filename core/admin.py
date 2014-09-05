from django.contrib import admin

from .models import Noticia, Site, Url


class NoticiaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Noticia, NoticiaAdmin)


class SiteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'site', 'start', 'tipo', 'status')
    list_filter = ('tipo', 'status')
    list_editable = ('status',)
    search_fields = ('nome', 'site')


admin.site.register(Site, SiteAdmin)


class UrlAdmin(admin.ModelAdmin):
    pass


admin.site.register(Url, UrlAdmin)