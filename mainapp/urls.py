from django.contrib import admin
from django.urls import re_path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    re_path(r'^$', mainapp.products, name='index'),
    re_path(r'^category/(\d+)/$', mainapp.products, name='category'),
    re_path(r'^category/(\d+)/page/(\d+)/$', mainapp.products, name='page'),

    re_path(r'^product/(\d+)/$', mainapp.product, name='product'),
]
