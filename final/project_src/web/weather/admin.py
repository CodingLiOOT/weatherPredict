from django.contrib import admin
from . import models
# Register your models here.
class PermissionModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'url']  # 展示的字段
    list_editable = ['url']  # 编辑的字段


admin.site.register(models.Permission, PermissionModelAdmin)
admin.site.register(models.Role)
admin.site.register(models.User)
