from django.contrib import admin

# Register your models here.

from website import models


class MomentAdmin(admin.ModelAdmin):
    empty_value_display = "空值"

class MomentAdmin1(admin.ModelAdmin):
    fields = ('content', 'kind', )


class MomentAdmin2(admin.ModelAdmin):
    exclude = ('user_name', )

class MomentAdmin(admin.ModelAdmin):
    fieldsets = (
        ("消息内容",{
            'fields':('content', 'kind', )
        }),
        ("用户信息",{
            'fields':('user_name',)
        }),
    )


class MyAdminSite(admin.AdminSite):
    site_header = "我的管理网站"


admin_site = MyAdminSite()
admin_site.register(models.Moment, MomentAdmin)

