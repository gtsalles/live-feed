from django.contrib import admin

from .models import Noticia, Site


class NoticiaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Noticia, NoticiaAdmin)


class SiteAdmin(admin.ModelAdmin):
    pass


admin.site.register(Site, SiteAdmin)
