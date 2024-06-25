from django.contrib import admin

from .models import Skill


class SkillAdmin(admin.ModelAdmin):
    list_display=('skill_name','percent','position','is_hidden')
    search_fields=('skill_name',)
admin.site.register(Skill,SkillAdmin)
