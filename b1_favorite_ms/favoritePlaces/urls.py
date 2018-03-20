from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^favorite/$', views.ListFavorite.as_view()),
    url(r'^favorite/(?P<pk>[0-9]+)/$', views.DetailFavourite.as_view())
]