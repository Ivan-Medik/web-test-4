from django.shortcuts import redirect


def redirect_blog(response):
    return redirect('posts_list_url', permanent=True)
