from django.conf.urls import url
from . import views

from .views import (
    ComponyListAPIView,
    ClientListAPIView,
    UserListAPIView,
    
    
    ComponyCreateAPIView,
    UserCreateAPIView,
    ClientCreateAPIView,
    
    

    ComponyADetailAPIView,
    UserADetailAPIView,
    


    UserDeleteAPIView,
    ComponyDeleteAPIView,

)


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^create/$', views.create, name='create'),
    url(r'^list/$', views.list, name='list'),

    #testing my urls
    url(r'^aime/$', views.aime, name='aime'),


    url(r'^signup/$', views.signup, name='signup'),


    url(r'^api/list/$', ComponyListAPIView.as_view(), name='list'),
    url(r'^client/list/api$', ClientListAPIView.as_view(), name='list'),
    url(r'^list/user/api$', UserListAPIView.as_view(), name='list'),
    
    


    url(r'^create/api/$', ComponyCreateAPIView.as_view(), name='create'),
    url(r'^create/client/api/$', ClientCreateAPIView.as_view(), name='create'),
    url(r'^user/create/api/$', UserCreateAPIView.as_view(), name='create'),
    

    
    url(r'^(?P<pk>\d+)/$', ComponyADetailAPIView.as_view(), name='detail'),
    url(r'^user(?P<pk>\d+)/$', UserADetailAPIView.as_view(), name='detail'),
    


    url(r'^user/delete/api(?P<pk>\d+)/$', UserDeleteAPIView.as_view(), name='delete'),
    url(r'^delete/api/(?P<pk>\d+)/$',
        ComponyDeleteAPIView.as_view(), name='delete'),

]
