from django.contrib import admin
from blog.models import Post

# Register your models here.


@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['title']
    }
    list_display = ['author', 'created', 'status', 'title']
    list_filter = ['author', 'created']
    ordering = ['-status', '-created']
    search_fields = ['author', 'title']
    raw_id_fields = ['author']