from PIL import Image
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver

from django.utils.safestring import mark_safe


class BaseModel(models.Model):
    name = models.CharField(max_length=60, verbose_name='Назва')
    image = models.ImageField(upload_to='base_page/image/', verbose_name='Фото')
    date = models.DateField(verbose_name='Дата')
    is_published = models.BooleanField(default=True, verbose_name='Публікація')

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.image.url))

    admin_photo.short_description = 'Фото'
    admin_photo.allow_tags = True

    def __str__(self):
        return " ".join([self.name, str(self.date)[5:]])

    def save(self):
        super().save()
        img = Image.open(self.image.path)

        if img.height > 700 or img.width > 1000:
            output_size = (700, 1000)
            img.thumbnail(output_size)
            img.save(self.image.path)

    class Meta:
        abstract = True


class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    description = models.TextField(max_length=1000, verbose_name='Опис')
    date = models.DateField(verbose_name='Дата')
    is_published = models.BooleanField(default=True, verbose_name='Публікація')

    class Meta:
        verbose_name_plural = 'Новини'
        ordering = ["-date"]

    def __str__(self):
        return self.title


class Bio(BaseModel):
    name = None
    title = models.CharField(max_length=60, verbose_name='Заголовок')
    description = models.TextField(max_length=1600, verbose_name='Опис')
    image = models.ImageField(upload_to='base_page/image/Bio', verbose_name='Фото')

    class Meta:
        verbose_name_plural = 'Біографія'

    def __str__(self):
        return self.title


class MyPhoto(BaseModel):
    image = models.ImageField(upload_to='base_page/image/MyPhoto', verbose_name='Фото')

    class Meta:
        verbose_name_plural = 'Мої Фото'
        ordering = ["-date"]


class PhotoAlbum(BaseModel):
    image = models.ImageField(upload_to='base_page/image/PhotoAlbum', verbose_name='Фото')

    class Meta:
        verbose_name_plural = 'Альбом'
        ordering = ["-date"]


class Video(models.Model):
    name = models.CharField(max_length=60, verbose_name='Назва')
    link = models.TextField(max_length=1500, verbose_name='Посилання')
    date = models.DateField(verbose_name='Дата')
    is_published = models.BooleanField(default=True, verbose_name='Публікація')

    class Meta:
        verbose_name_plural = 'Відео'
        ordering = ["-date"]

    def __str__(self):
        return " ".join([self.name, str(self.date)[5:]])


@receiver(pre_delete, sender=Bio)
@receiver(pre_delete, sender=MyPhoto)
@receiver(pre_delete, sender=PhotoAlbum)
def delete_image(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    if instance.image:
        instance.image.delete(False)
