from django.db import models
from django.utils import timezone 
from django.contrib.auth import get_user_model
from stdimage.models import StdImageField

class Post(models.Model):
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)
    author = models.ForeignKey(get_user_model(), verbose_name='author', on_delete=models.CASCADE , null=True, blank=True)
    title = models.CharField('Titulo',max_length=200)
    desc = models.TextField('Descrição', null=True, blank=True)
    image = StdImageField('Imagem', upload_to='post/imagem', variations={'thumb': (250, 250, True)}, delete_orphans = True, blank=True)
    download_file = models.FileField(upload_to='post/file', null=True, blank=True) 
    download_link = models.CharField('Link Download',max_length=200, null=True, blank=True) 
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


