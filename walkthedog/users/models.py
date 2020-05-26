from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from easy_thumbnails.fields import ThumbnailerImageField


class User(AbstractUser):
    IS_WHO_CHOICE = (
        ('is_client', "I'm client"),
        ('is_dog_sitter', "I'm dog sitter"),
    )

    # First Name and Last Name do not cover name patterns
    # around the globe.
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(_('username'), max_length=30, unique=True,
                                help_text=_('Required. 30 characters or fewer. Letters, numbers and '
                                            '@/./+/-/_ characters'),
                                validators=[username_validator])
    email = models.EmailField(_('Email address'), max_length=30, unique=True)
    first_name = models.CharField('First name', max_length=120)
    last_name = models.CharField('Last name', max_length=120)
    phone_number = models.CharField('Phone number', max_length=15, unique=True, default=0)
    image = ThumbnailerImageField('Photo', upload_to='photos', blank=True)
    who_choice = models.CharField(max_length=30, choices=IS_WHO_CHOICE,
                                  default=IS_WHO_CHOICE[0][0], verbose_name='')
    description = models.TextField('About myself', default='', blank=True)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
