from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager 
from stdimage.models import StdImageField

class UserManager(BaseUserManager):
        use_in_migrations = True

        def _create_user(self, email, password, **extra_fields):

                if not email:
                        raise ValueError('E-mail é obrigatório')

                email = self.normalize_email(email)
                user = self.model(email=email, username=email, **extra_fields)
                user.set_password(password)
                user.save(using=self._db)
                print("usermanager")
                return user

        def create_user(self, email, password=None, **extra_fields):

                extra_fields.setdefault('is_superuser', False)
                return self._create_user(email, password, **extra_fields)

        def create_superuser(self, email, password, **extra_fields):

                extra_fields.setdefault('is_superuser', True)
                extra_fields.setdefault('is_staff', True)

                if extra_fields.get('is_superuser') is not True:
                        raise ValueError('Superuser need to be is_superuser=True')

                if extra_fields.get('is_staff') is not True:
                        raise ValueError('Superuser need to be is_staff=True')

                return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
        TYPE_USER_CHOICES = [('ad', 'Administrador'),('co', 'Colaborador'),('us', 'Usuario Padrão')] 
        email = models.EmailField('Email', unique=True) 
        type_user = models.CharField('type_user',max_length=2,choices=TYPE_USER_CHOICES) 
        
        is_staff = models.BooleanField('Team member', default=True)
        is_active = models.BooleanField('active', default=False)
        date_joined = models.DateTimeField('date joined', auto_now_add=True)

        imagem = StdImageField('Imagem', upload_to='perfil', variations={'thumb': (100, 100, True)}, delete_orphans = True, blank=True)
        slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)
 
        USERNAME_FIELD = 'email'
        REQUIRED_FIELDS = ['first_name', 'last_name', 'type_user', 'is_active']

        class Meta:
                verbose_name = 'Usuário'
                verbose_name_plural = 'Usuários'
                ordering = ['first_name']

        def __str__(self):
                return self.email

        objects = UserManager() 