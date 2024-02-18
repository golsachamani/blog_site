from django.contrib import admin
from . models import Post
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status',)
    ordering = ('status',)# if we sorting or ordering as desc we should use -->('-status')
#admin.site.register(Post, PostAdmin)

