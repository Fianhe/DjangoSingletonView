from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from example.views import SingletonView
from django.conf import settings
from django.conf.urls import patterns

# rrr = DefaultRouter()
# rrr.register('singleton', SingletonView, 'singleton')


urlpatterns = [
    url(r'^$', SingletonView.as_view({'get':'list', 'post': 'create', 'delete': 'destroy', 'put': 'update'})),
]