from django.contrib import admin
from .models import Post, Comment, PostNumber, PostTopic, PostCommentator

# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(PostNumber)
admin.site.register(PostTopic)
admin.site.register(PostCommentator)