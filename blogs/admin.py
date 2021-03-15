from django.contrib import admin
from .models import Post

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')


admin.site.register(Post, AuthorAdmin)