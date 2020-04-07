from django.shortcuts import redirect
from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import View

from .models import Post, Tag
from .utils import *
from .forms import TagForm, PostForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

from django.db.models import Q

import datetime

def posts_list(request):
    search_querry = request.GET.get('search','')

    if search_querry:
        posts = Post.objects.filter(Q(title__icontains=search_querry) | Q(body__icontains=search_querry))
    else:
        posts = Post.objects.all()

    for post in posts:
        post_list = list(str(post.date_pub))
        time_now_list = list(str(datetime.date.today()))
        for i in range(22):
            del post_list[-1]
        for i in range(8):
            del post_list[0]
            del time_now_list[0]
        if post_list[0] == "0":
            del post_list[0]
        if time_now_list[0] == "0":
            del time_now_list[0]
        text_p = ""
        for el in post_list:
            text_p += el
        text_n = ""
        for el in time_now_list:
            text_n += el
        if int(text_p) <= int(text_n):
            new = True

        context = {
            'posts': posts,
            'new': new,
        }

    return render(request, 'blog/index.html', context=context)

# def contact(request):
#     return render(request, 'blog/news_detail.html')

class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model_form = PostForm
    template = 'blog/post_create_form.html'
    raise_exception = True


class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Post
    model_form = PostForm
    template = 'blog/post_update_form.html'
    raise_exception = True


class PostDelete(LoginRequiredMixin,ObjectDeleteMixin, View):
    model = Post
    template = 'blog/post_delete_form.html'
    redirect_url = 'posts_list_url'
    raise_exception = True


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model_form = TagForm
    template = 'blog/tag_create.html'
    raise_exception = True


class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Tag
    model_form = TagForm
    template = 'blog/tag_update_form.html'
    raise_exception = True


class TagDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Tag
    template = 'blog/tag_delete_form.html'
    redirect_url = 'tags_list_url'
    raise_exception = True


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})
