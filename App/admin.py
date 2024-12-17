from django.contrib import admin
from .models import Posts


class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'description')
    search_fields = ('title', 'created_at', 'description')
    ordering = ('-created_at',)

admin.site.register(Posts, PostsAdmin)
