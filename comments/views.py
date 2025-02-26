from django.shortcuts import render, redirect, get_object_or_404
from .forms import CommentForm
from articles.models import Article
from django.contrib.auth.decorators import login_required
from django.urls import reverse

@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Article, id=post_id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            # Success redirect
            return redirect('article_detail', pk=post_id)
    else:
        form = CommentForm()

    return render(request, 'comments/add_comment.html', {'form': form})
