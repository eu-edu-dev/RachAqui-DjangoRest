from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from image_cropping import ImageCropField, ImageRatioField

from base.models import BaseModel, Company, Person
from base_settings import settings


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email must be set')

        if not password:
            raise ValueError('Password must be set')

        email = self.normalize_email(email)
        user: "AbstractBaseUser" = self.model(
            email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):

    # role = models.CharField(max_length=50, choices=Role.choices)
    email = models.EmailField('email address', max_length=255, unique=True)
    is_staff = models.BooleanField('staff status', default=False,
                                   help_text='Designates whether the user can log into this admin site.')
    is_active = models.BooleanField('active', default=True,
                                    help_text='''Designates whether this user should be treated as active.
                                     Unselect this instead of deleting accounts.''')

    date_joined = models.DateTimeField('date joined', default=timezone.now)
    is_trusty = models.BooleanField('trusty', default=False,
                                    help_text='Designates whether this user has confirmed his account.')

    # profile_image = ImageCropField('Fotografia', upload_to=texto_upload_path, blank=True, null=True,
    #                                storage=PublicMediaStorage())
    # cropping = ImageRatioField(
    #     'profile_image', '200x200', verbose_name='Avatar', size_warning=True,
    #     help_text='''A configuração do Avatar é possível após a atualização da fotografia.''')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ['-email']

    def get_full_name(self):
        return

    def get_short_name(self):
        return self.get_full_name()

    # @cached_property
    # def drf_token(self):
    #     return Token.objects.get_or_create(user=self)

    def email_user(self, subject, message, from_email=settings.EMAIL_SEND_USER):
        send_mail(subject, message, from_email, [self.email])

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)

    def __str__(self):
        return self.email
