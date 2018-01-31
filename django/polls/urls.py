from django.urls import path, re_path

from polls import views

urlpatterns = [
    # re_path(r'^$', views.index, name='index'),
    path('', views.index),
]