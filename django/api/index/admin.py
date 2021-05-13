from django.contrib import admin
from .models import UserData,Push,Support,General
from django.contrib.auth.admin import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

class UserProfileInline(admin.StackedInline):
    model = UserData 
    max_num = 1
    can_delete = False

class UserAdmin(AuthUserAdmin):
    inlines = [UserProfileInline]

# unregister old user admin
admin.site.unregister(User)
# register new user admin
admin.site.register(User, UserAdmin)

@admin.register(UserData)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','user','number','location','avatar','blocked')
    search_fields = ("location__startswith", )
    list_filter = ('location', )

@admin.register(Push)
class PushAdmin(admin.ModelAdmin):
    list_display = ('id','title','describe','slug')
    search_fields = ("slug__startswith", )

@admin.register(Support)
class SupportAdmin(admin.ModelAdmin):
    list_display = ('id','user','title','describe','active')
    search_fields = ("title__startswith", )
    list_filter = ('user','active', )

@admin.register(General)
class GeneralAdmin(admin.ModelAdmin):
    pass