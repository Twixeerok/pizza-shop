import imghdr
from statistics import mode
from turtle import title
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class MainPageMenu(models.Model):
    title = models.CharField(verbose_name='Название пиццы', max_length=50)
    text = models.CharField(verbose_name='Описание пиццы',max_length=100)
    full_tex = models.TextField(verbose_name='состав')
    img = models.ImageField(verbose_name='Картинка', upload_to="img/")
    slug = models.SlugField(unique=True, verbose_name="URL")

    def get_absolute_url(self):
        return reverse('qui:pk', kwargs={"slug": self.slug})
    
    
    
    def __str__(self):
        return self.title

    class Meta:

        verbose_name = "Меню"
        verbose_name_plural = "Меню"

class Comments(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    posts = models.ForeignKey(MainPageMenu, null=True, on_delete=models.CASCADE)
    comment = models.TextField(verbose_name='Комментарий')

    def __str__(self) -> str:
        return self.comment
    
    class Meta:
        verbose_name = "Коментраии"
        verbose_name_plural = "Коментраии"