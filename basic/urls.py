from django.conf.urls import patterns, url
from basic import views

urlpatterns = patterns('',
                url(r'^$', views.index, name='index'),
                
                )

