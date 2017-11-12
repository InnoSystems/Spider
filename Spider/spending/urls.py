'''
Created on 23.09.2017

@author: Adrian
'''

from django.conf.urls import url

from . import views

app_name = 'spend'
urlpatterns = [
    # ex: /spending/
    url(r'^$', views.index, name='index'),
    # ex: /spending/3/  
    url(r'^(?P<shopping_id>[0-9]+)/$', views.getShoppingById, name='detail'),
    # ex: /spending/5/results/
    url(r'^(?P<shopping_id>[0-9]+)/results/$', views.result, name='results'),
    # ex: /spending/detail/3/
    url(r'^detail/(?P<shopping_id>[0-9]+)/$', views.detail, name='detailnew'),
    # ex: /spending/3/vote/
    url(r'^(?P<shopping_id>[0-9]+)/vote/$', views.vote, name='vote')
]   