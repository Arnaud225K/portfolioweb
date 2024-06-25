from django.contrib import admin

from .models import Portfolio, TypePorfolio, ImageGallery


class TypePorfolioAdmin(admin.ModelAdmin):
    list_display=('name',)
    search_fields=('name',)
admin.site.register(TypePorfolio,TypePorfolioAdmin)

class ImageGalleryAdmin(admin.TabularInline):
    model = ImageGallery

class PorfolioAdmin(admin.ModelAdmin):
    inlines = (ImageGalleryAdmin,)
    list_display=('type_porfolio','title','is_hidden',)
    search_fields=('title',)
    list_filter = ('type_porfolio','is_hidden',)
admin.site.register(Portfolio,PorfolioAdmin)

