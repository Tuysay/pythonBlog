from django.contrib import admin
from .models import Post, Commit
# Register your models here.



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')


@admin.register(Commit)
class CommitAdmin(admin.ModelAdmin):
    list_display = ('name', 'post')
