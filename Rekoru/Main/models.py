from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,            
        )

        user.set_password(password)        
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,            
        )
        user.is_staff = True
        user.is_superuser = True   
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    username = models.CharField(verbose_name='name', max_length=30, blank=True)
    is_staff = models.BooleanField(verbose_name='staff', default=False)
    avatar = models.ImageField(verbose_name='avatar', upload_to='avatar/%Y-%m-%d/', blank=True, default='avatar_user.svg')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_full_name(self):
        return self.username

    def __str__(self):
        return '{} <{}>'.format(self.username, self.email)

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


class AddprojectModel(models.Model):
    title = models.CharField(verbose_name='title', max_length=255, unique=True)
    description = models.TextField(verbose_name='text')
    imageproject = models.ImageField(upload_to='project-images/avatar/%Y-%m-%d/')
    comments = models.TextField(verbose_name='comments', blank=True)

