from django.contrib import admin
from .models import Menu, Link


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    fields = ['title', 'href', 'order']


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    fields = ['title', 'href', 'order', 'icon']


# 设置标题
admin.site.site_header = '卿志宇 - 后台管理'
admin.site.site_title = '卿志宇'
