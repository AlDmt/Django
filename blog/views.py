from django.shortcuts import render, get_object_or_404
from blog.models import Post


# Create your views here.
# Все опубликованные посты
def post_list(request):
    posts = Post.objects.filter(status=Post.PostStatus.PUBLISHED)
    return render(request, 'blog/post/list.html', {'posts':posts})

# Один конкретный пост
def post_detail(request, year, month, day, posts):
    post=get_object_or_404(Post, slug=post,
                           status='published',
                           publish_year=year,
                           publish_month=month,
                           publish_day=day)
    return render(request,'blog/post/detail.html', {'post':post})

