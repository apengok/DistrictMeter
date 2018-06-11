# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from .utils import code_generator


User = settings.AUTH_USER_MODEL

class ProfileManager(models.Manager):
    def toggle_follow(self, request_user, username_to_toggle):
        profile_ = Profile.objects.get(user__username__iexact=username_to_toggle)
        user = request_user
        is_following = False
        if user in profile_.followers.all():
            profile_.followers.remove(user)
        else:
            profile_.followers.add(user)
            is_following = True
        return profile_, is_following

class Profile(models.Model):
    user         = models.OneToOneField(User) # user.profile
    real_name    = models.CharField(_('real name'), max_length=30, blank=True)
    sex          = models.CharField(_('Sex'), max_length=30, blank=True)
    phone_number = models.CharField(_('phone number'), max_length=30, blank=True)
    belongto     = models.CharField(_('belongs to'), max_length=30, blank=True)
    expire_date  = models.CharField(_('Expired date'), max_length=30, blank=True)
    Role         = models.CharField(_('Role'), max_length=30, blank=True)
    

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        blank=True,
    )

    objects = ProfileManager()

    def __str__(self):
        return self.user.username

    def send_activation_email(self):
        if not self.activated:
            self.activation_key = code_generator()# 'somekey' #gen key
            self.save()
            #path_ = reverse()
            path_ = reverse('activate', kwargs={"code": self.activation_key})
            full_path = "https://muypicky.com" + path_
            subject = 'Activate Account'
            from_email = settings.DEFAULT_FROM_EMAIL
            message = 'Activate your account here: {}'.format(full_path)
            recipient_list = [self.user.email]
            html_message = '<p>Activate your account here: {}</p>'.format(full_path)
            print(html_message)
            sent_mail = send_mail(
                            subject, 
                            message, 
                            from_email, 
                            recipient_list, 
                            fail_silently=False, 
                            html_message=html_message)
            sent_mail = False
            return sent_mail




def post_save_user_receiver(sender, instance, created, *args, **kwargs):
    if created:
        profile, is_created = Profile.objects.get_or_create(user=instance)
        default_user_profile = Profile.objects.get_or_create(user__id=1)[0] #user__username=
        default_user_profile.followers.add(instance)
        #profile.followers.add(default_user_profile.user)
        #profile.followers.add(2)

post_save.connect(post_save_user_receiver, sender=User)
# Create your models here.
