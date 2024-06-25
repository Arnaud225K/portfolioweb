from django.contrib import admin

from .models import Service


class ServiceAdmin(admin.ModelAdmin):
    list_display=('service_name','title','modified_date','is_hidden')
    search_fields=('service_name',)
admin.site.register(Service,ServiceAdmin)