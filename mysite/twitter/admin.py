from django.contrib import admin

from .models import Post

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['username']}),
        (None,               {'fields': ['post_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

admin.site.register(Post, PostAdmin)
