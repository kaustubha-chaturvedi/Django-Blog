from django.contrib import admin
from .models import Post,Comment
# Register your models here.
@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','content'] # this variable sets sequence of key to diplay in django admin area

@admin.register(Comment)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['post','date_added','com'] # 'com' here is comment I think I was high when I named it.