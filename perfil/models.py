from django.db.models.signals import post_save
from django.dispatch import receiver 
from django.db import models 
from stdimage.models import StdImageField    
from accounts.models import CustomUser
from perfil.choices import SocialNetwork

class Profile(models.Model):   
    user = models.OneToOneField(CustomUser,  on_delete=models.DO_NOTHING, related_name='profile') 
    image = StdImageField('Image', upload_to='profile', variations={'thumb': (500, 500, True)}, delete_orphans = True, blank=True) 
    
    occupation = models.CharField(max_length=120)
    description = models.TextField()  
    gender = models.CharField(max_length=20, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=20, blank=True) 

    def __str__(self):
        return f' Profile: {self.user.username}'

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
  
    @receiver(post_save, sender=CustomUser)
    def create_profile(sender, **kwargs):
        if kwargs.get('created', False):
            Profile.objects.create(user=kwargs['instance'])

class Network(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="network", blank=True, null=True) 
    name = models.CharField(max_length=10, choices=SocialNetwork.choices, blank=True, null=True) 
    url = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Network"
        verbose_name_plural = "Networks"


    @receiver(post_save, sender=Profile)
    def create_network(sender, **kwargs): 
        profile = kwargs['instance']
        if kwargs.get('created', False):  
            # for v in SocialNetwork:
            #     print(v)  
            #     Network.objects.create(profile=kwargs['instance'])  
           for i in SocialNetwork:
                Network.objects.create(name=i, profile=kwargs['instance']) 
         