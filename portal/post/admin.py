from django.contrib import admin
from post.models import Post, Category, SocialComment
# Register your models here.

admin.site.register(Post) 
admin.site.register(Category)
admin.site.register(SocialComment)