from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.contrib.auth.forms import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    avatar = models.ImageField('Аватар', upload_to='static/images/profiles', blank=True)
    phone = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=40)
    slug = models.SlugField(max_length=50, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("profile", kwargs={"slug": User.username})

    class Meta:
        verbose_name = "Профиль"


@receiver(post_save, sender=User)
def save_or_create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        try:
            instance.profile.save()
        except ObjectDoesNotExist:
            Profile.objects.create(user=instance)
