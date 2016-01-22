from django.contrib import admin
from blog.models import BlogPost,Tag

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','publish_time',)
    
class TagAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Tag,TagAdmin)