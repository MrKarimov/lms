from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from .models import Article
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, 
    DetailView,
    DeleteView, 
    UpdateView,
    CreateView
    )
#barcha bloglarni bir pageda chiqarish uchun View
class ArticlesListView(LoginRequiredMixin,ListView):
    model = Article
    template_name = "article/article_list.html"


#blogni to'liq xolatda ochish uchun View
class ArticleDetailView(LoginRequiredMixin,DetailView):
    model = Article
    template_name = 'article/article_detail.html'
    context_object_name = 'article'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_posts'] = Article.objects.exclude(pk=self.object.pk).order_by('-date')[:5]
        return context

#blogni tahrirlash uchun View
class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model = Article
    fields = ('title', 'summary', 'photo', 'body',)
    template_name = 'article/article_edit.html'

    def test_func(self) -> bool | None:
        return self.request.user.is_superuser


#Blogni o'chirish uchun View
class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'article/article_delete.html'
    success_url   = reverse_lazy('article_list')

    def test_func(self):
        return self.request.user.is_superuser
    
#yangi  blog yaratish uchun View
class ArticleCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Article
    fields = ('title', 'summary', 'body', 'photo')
    template_name = 'article/article_create.html'

    def test_func(self):
        return self.request.user.is_superuser


    #ushbu qisim yaratilayotgan blog mulifini avtomatik ko'rsatish vazifasini bajaradi
    def form_valid(self, form) :
        form.instance.author = self.request.user
        return super().form_valid(form)