from django.db import models
from django.utils import timezone 
from django.contrib.auth import get_user_model
from stdimage.models import StdImageField

class Category(models.Model):
    name = models.CharField('Category',max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = verbose_name
  
class Tag(models.Model):
    name = models.CharField('Tags',max_length=100)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "tag"
        verbose_name_plural = "tags"
 
class Post(models.Model):
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)
    author = models.ForeignKey(get_user_model(), verbose_name='author', on_delete=models.CASCADE , null=True, blank=True)
    title = models.CharField('Titulo',max_length=200)
    desc = models.TextField('Descrição', null=True, blank=True)
    image = StdImageField('Imagem', upload_to='post/imagem', variations={'thumb': (420, 280, True)}, delete_orphans = True, blank=True)
    download_file = models.FileField(upload_to='post/file', null=True, blank=True) 
    download_link = models.CharField('Link Download',max_length=200, null=True, blank=True) 
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    category = models.ForeignKey(Category, verbose_name="Category", on_delete=models.CASCADE, null=True, blank=True)
    tags = models.ManyToManyField(Tag, verbose_name="Tag", null=True, blank=True)
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