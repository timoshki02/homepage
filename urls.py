from django.conf.urls import include, url
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^homepage/$', views.home , name = 'home'),
    url(r'^newspage/$', views.news , name = 'news'),
    url(r'^newspage/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'\
    	r'(?P<slug>[-\w]+)/$',views.news_detail,name = 'detail'),
]