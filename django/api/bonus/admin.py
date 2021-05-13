from django.contrib import admin
from .models import Info,Questions,Invation

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
