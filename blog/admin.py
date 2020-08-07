from django.contrib import admin
from .models import Category, Tag, Article, Menu, Link


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_time', 'modified_time', 'author')


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
