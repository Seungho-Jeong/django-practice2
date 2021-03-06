from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.core.validators import RegexValidator
from django.db import models
from django.template.loader import render_to_string
from django.shortcuts import resolve_url


class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = 'm', 'Male'
        FEMALE = 'f', 'Female'
        NON_BINARY = 'nb', 'Non-binary'
        TRANSGENDER = 'tr', 'Transgender'
        INTERSEX = 'in', 'Intersex'
        NOT_SAY = 'ns', 'I prefer not to say'

    website_url = models.URLField(blank=True)
    bio = models.TextField(blank=True)
    phone_number = models.CharField(max_length=13, validators=[RegexValidator(r"^01[01679]-?\d{3,4}-?\d{4}$")],
                                    blank=True)
    gender = models.CharField(max_length=2, choices=GenderChoices.choices, blank=True)
    avatar = models.ImageField(upload_to="accounts/avatar/%Y/%m/%d", blank=True,
                               help_text="48px * 48px 크기의 '.png' 또는 '.jpg' 파일을 업로드 해주세요.")
    follower_set = models.ManyToManyField('self', blank=True)
    following_set = models.ManyToManyField('self', blank=True)

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def avatar_url(self):
        if self.avatar:
            return self.avatar.url
        else:
            return resolve_url("pydenticon_image", self.username)

    def send_welcome_email(self):
        subject = render_to_string("accounts/welcome_email_subject.txt", {"user": self})
        content = render_to_string("accounts/welcome_email_content.txt", {"user": self})
        from_email = settings.WELCOME_EMAIL_SENDER
        send_mail(subject, content, from_email, [self.email], fail_silently=False)
