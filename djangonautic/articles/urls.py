
from django.urls import path, re_path
from .import views


app_name = 'articles'

urlpatterns = [
    re_path(r'^$', views.articles_list, name="list"),
    re_path(r'^create/$', views.article_create, name="create"),
    re_path(r'^(?P<slug>[\w-]+)/$', views.articles_details, name="details"),
]