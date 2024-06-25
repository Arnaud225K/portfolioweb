from django.contrib import admin
from .models import TypeQuality, Quality


class TypeQualityAdmin(admin.ModelAdmin):
    list_display=('name',)
    search_fields=('name',)
admin.site.register(TypeQuality,TypeQualityAdmin)

class QualityAdmin(admin.ModelAdmin):
    list_display=('quality_name','type_quality','location','started_at','ended_at','is_hidden',)
    search_fields=('quality_name',)
    list_filter = ('type_quality','is_hidden',)
admin.site.register(Quality,QualityAdmin)
