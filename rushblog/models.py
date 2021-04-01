from django.db import models
from ckeditor.fields import RichTextField
class Post(models.Model): #Storing Posts
    title = models.TextField(max_length=200)
    content = RichTextField()

    def __str__(self):
        return self.title

class Comment(models.Model): #Storing Comment
    # ForeignKey Implementation links post and comments to each other
    post=models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE) 
    name=models.TextField(max_length=150)
    com=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)