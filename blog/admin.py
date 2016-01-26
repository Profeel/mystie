# -*- coding: utf-8 -*-”
from django.contrib import admin
from blog.models import BlogPost,Tag

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','publish_time',)
    # 添加搜索项，按照title进行搜索
    search_fields = ['title']
    
class TagAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Tag,TagAdmin)