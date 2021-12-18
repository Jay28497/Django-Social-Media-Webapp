from django.contrib import admin
from mainApp.models import Post, Like, Dislike, Comment, SubComment

# Register your models here.
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Dislike)
admin.site.register(Comment)
admin.site.register(SubComment)
