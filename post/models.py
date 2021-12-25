from django.db import models
from django.utils import timezone 
from django.contrib.auth import get_user_model 
from stdimage.models import StdImageField 
from taggit.managers import TaggableManager
import uuid 

class Category(models.Model):
    name = models.CharField('Category',max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = verbose_name
    
class Post(models.Model):  
    author = models.ForeignKey(get_user_model(), verbose_name='author', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField('Titulo',max_length=200)
    desc = models.TextField('Descrição', null=True, blank=True)
    image = StdImageField('Imagem', upload_to='post/imagem', variations={'thumb': (420, 280, True)}, delete_orphans = True, blank=True)
    
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True) 
    is_activate = models.BooleanField('activate',default=False) 
    
    download_file = models.FileField(upload_to='post/file', null=True, blank=True) 
    download_link = models.CharField('Link Download',max_length=200, null=True, blank=True) 
     
    category = models.ForeignKey(Category, verbose_name="Category", on_delete=models.CASCADE, null=True, blank=True)
    tags = TaggableManager()
     
    likes = models.ManyToManyField(get_user_model(), blank=True, related_name='likes')
    dislikes = models.ManyToManyField(get_user_model(), blank=True, related_name='dislikes')

    views = models.PositiveIntegerField(default=0, editable=False) 

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
 
    @property
    def get_photo_url(self):
        if self.author.imagem and hasattr(self.author.imagem, 'url'):
            return self.author.imagem.url
        else:
            return "/static/images/default.png"
  
class SocialComment(models.Model):
    comment = models.TextField()
    created_on = models.DateTimeField(default=timezone.now) 
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='social_comment_author')
    post = models.ForeignKey(Post, on_delete=models.CASCADE) 
    likes = models.ManyToManyField(get_user_model(), blank=True, related_name='comment_likes')
    dislikes = models.ManyToManyField(get_user_model(), blank=True, related_name='comment_dislikes')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='+')

    @property
    def children(self):
        return SocialComment.objects.filter(parent=self).order_by('-created_on').all()

    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False