from django.contrib import admin
from .models import Post,Comment
# Register your models here.
@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','content']

@admin.register(Comment)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['post','date_added','com']