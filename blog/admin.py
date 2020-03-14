from django.contrib import admin
from .models import Blog, BlogTag


# Register your models here.
@admin.register(BlogTag)
class BlogTagAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag_name')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'tags', 'author', 'created_time',
                    'get_read_num', 'last_update_time')


# @admin.register(ReadNum)
# class ReadNumAdmin(admin.ModelAdmin):
#     list_display = ('read_num', 'blog')
