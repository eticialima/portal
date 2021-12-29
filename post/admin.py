from django.contrib import admin
from post.models import Post, Category, SocialComment

admin.site.register(Post) 
admin.site.register(Category)
admin.site.register(SocialComment)