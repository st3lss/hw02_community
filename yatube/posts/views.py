from django.shortcuts import render, get_object_or_404

from .models import Post, Group


def index(request):
    template = 'posts/index.html'
    title = 'Последние обновления на сайте'
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'title': title,
        'posts': posts,
    }

    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    title = f'Записи сообщества {group.title}'
    template = 'posts/group_list.html'
    posts = Post.objects.select_related('author', 'group').all()[:10]
    context = {
        'title': title,
        'group': group,
        'posts': posts,
    }

    return render(request, template, context)
