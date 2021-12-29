from django.db import models 

class SocialNetwork(models.TextChoices):
    YOUTUBE = 'YOUTUBE', 'youtube' 
    WHATSAPP = 'WHATSAPP', 'whatsapp' 
    FACEBOOK = 'FACEBOOK', 'facebook' 
    INSTAGRAM = 'INSTAGRAM', 'instagram' 
    TWITTER = 'TWITTER', 'twitter' 
    PINTEREST = 'PINTEREST', 'pinterest' 
    SNAPCHAT = 'SNAPCHAT', 'snapchat' 
    TIKTOK = 'TIKTOK', 'tiktok' 
    DISCORD = 'DISCORD', 'discord' 
    GITHUB = 'GITHUB', 'Github'  