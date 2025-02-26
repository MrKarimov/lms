from django.shortcuts import render, get_object_or_404, redirect
from admin_dashboard.forms import ArticleForm, CustomUserForm, CommentForm
from articles.models import Article
from accounts.models import CustomUser
from comments.models import Comment
from admin_dashboard.models import Action

def custom_admin_view(request):
    articles = Article.objects.all()
    accounts = CustomUser.objects.all()
    comments = Comment.objects.all()
    recent_actions = Action.objects.all()[:10]
    return render(request, 'custom_admin/admin_dashboard.html', {
        'accounts': accounts,
        'articles': articles,
        'comments': comments,
        'recent_actions': recent_actions,
    })

def edit_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('custom_admin_view')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'custom_admin/edit_article.html', {'form': form})

def edit_custom_user(request, pk):
    account = get_object_or_404(CustomUser, pk=pk)
    if request.method == "POST":
        form = CustomUserForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            return redirect('custom_admin_view')
    else:
        form = CustomUserForm(instance=account)
    return render(request, 'custom_admin/edit_custom_user.html', {'form': form})

def edit_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('custom_admin_view')
    else:
        form = CommentForm(instance=comment)
    return render(request, 'custom_admin/edit_comment.html', {'form': form})
