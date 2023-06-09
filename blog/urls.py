from django.urls import path, re_path
from . import views

urlpatterns = [

    path('', views.post_list, name='post_list'),

# Переход на конкретный пост
    re_path(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
            views.post_detail,
            name='post_detail'),
]