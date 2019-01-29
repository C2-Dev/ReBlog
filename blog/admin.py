from django.contrib import admin
from .models import Category, Post, Tag, TweetThread, Profile

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(TweetThread)
admin.site.register(Profile)