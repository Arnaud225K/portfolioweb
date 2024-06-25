from django.contrib import admin
from .models import Language, Owner, Picture, Sociallink, Function,Review


class FunctionAdmin(admin.TabularInline):
    model = Function

class SociallinkAdmin(admin.TabularInline):
    model = Sociallink

class LanguageAdmin(admin.TabularInline):
    model = Language

class PictureAdmin(admin.TabularInline):
    model = Picture

class OwnerAdmin(admin.ModelAdmin):
    inlines = (LanguageAdmin, SociallinkAdmin, FunctionAdmin, PictureAdmin)
    list_display=('fullname','degree','email','phone','freelance','is_hidden')
    search_fields = ('fullname',)
    list_filter = ('is_hidden','freelance',)
admin.site.register(Owner,OwnerAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display=('name','profession','company','message','is_hidden')
    search_fields = ('name','company','profession')
    list_filter = ('is_hidden',)
admin.site.register(Review,ReviewAdmin)