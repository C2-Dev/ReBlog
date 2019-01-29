from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Category(models.Model):
        name = models.CharField(max_length=32)

        def __str__(self):
                return self.name

class Tag(models.Model):
        name = models.CharField(max_length=32)

        def __str__(self):
                return self.name

class TweetThread(models.Model):
        tweet = models.URLField()

class Post(models.Model):
        author = models.OneToOneField(User, related_name='author', on_delete=models.CASCADE)
        category = models.ManyToManyField(Category)
        #title = models.CharField(max_length=64,unique=True)
        tweet = models.ForeignKey(TweetThread, related_name='ptweet', on_delete=models.CASCADE)
        #symbol = models.CharField(max_length=2)
        tags = models.ManyToManyField(Tag)
        views = models.PositiveIntegerField(default=0)
        #byline = models.CharField(max_length=255)
        #background_image = models.URLField(verify_exists=True)
        slug = models.SlugField(max_length=128)
        content = models.TextField()
        #updated_on = models.DateField(auto_now=True)
        created_on = models.DateField(auto_now_add=True)
        #publish_on = models.DateField()
        list_display = ('category', 'tags', 'author','created_on')
        search_fields = ['category','tags','author']
        list_filter = ['created_on']
        date_hierarchy = 'created_on'

        def __str__(self):
                return self.id

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    pic_url = models.TextField(null=True, max_length=150, blank=True,
                               default="https://bankwatch.org/wp-content/uploads/2018/03/Portrait_Placeholder.png")
    banner_url = models.TextField(null=True, max_length=150, blank=True,
                                  default="https://steamcdn-a.akamaihd.net/steamcommunity/public/images/items/566020/bba5cf5acb1e03045d81555821b986c7461ca64c.jpg")
    motto = models.TextField(null=True, max_length=100, blank=True)
    bday = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.user)