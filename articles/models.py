from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from ckeditor.fields import RichTextField 
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=200, blank = True)
    body    = RichTextField()
    photo   = models.ImageField(upload_to='images/',blank = True)
    date    = models.DateTimeField(auto_now_add=True)
    author  = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    #bloglar admin panelda title bilan ko'rsatiladi
    def __str__(self):
        return self.title
    
# reverse('article_detail', kwargs={'pk': self.pk}) qismi article_detail nomli URL manzilini pk (primary key) parametr bilan yaratuvchi funksiya hisoblanadi.
# self.pk qismi modelning asosiy kaliti (primary key) bo'lib, u ma'lum bir model ob'ektining yagona identifikatori hisoblanadi.
# misol uchun id bizning postlarda id bu primary key unikal biz shu postga murojat qilganda shu id orqli murojat ilamiz .
    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'pk': self.pk})