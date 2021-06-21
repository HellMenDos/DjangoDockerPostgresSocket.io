from django.contrib import admin
from .models import Info,Questions,Invation,Bonus,BonusGeneral,RelationBonus

@admin.register(Info)
class PushAdmin(admin.ModelAdmin):
    list_display = ('id','title','date')
    search_fields = ("title__startswith", )
    list_filter = ('title', )

@admin.register(Questions)
class PushAdmin(admin.ModelAdmin):
    list_display = ('id','title','date')
    search_fields = ("title__startswith", )
    list_filter = ('title', )

@admin.register(Invation)
class InvationAdmin(admin.ModelAdmin):
    list_display = ('id','user','hashurl','count')
    search_fields = ("hashurl__startswith", )

@admin.register(Bonus)
class BonusAdmin(admin.ModelAdmin):
    list_display = ('id','level','location','title','forUser')
    search_fields = ("title__startswith", )
    list_filter = ('location','forUser' )

@admin.register(BonusGeneral)
class BonusAdmin(admin.ModelAdmin):
    list_display = ('id','level','title','forUser')
    search_fields = ("title__startswith", )
    list_filter = ('level','forUser' )

@admin.register(RelationBonus)
class BonusAdmin(admin.ModelAdmin):
    list_display = ('id','user','bonus')
    list_filter = ('user','bonus' )
