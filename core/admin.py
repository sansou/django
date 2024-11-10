from django.contrib import admin
from core.models import Tag, Video

class VideoAdmin(admin.ModelAdmin):
    readonly_fields = ('published_at','num_likes', 'num_views')
    list_display = ('title', 'is_published', 'published_at', 'num_likes', 'num_views')
    search_fields = ('title', 'description' 'tags__name')
    list_filter = ('is_published', 'tags')

admin.site.register(Video, VideoAdmin)
admin.site.register(Tag)