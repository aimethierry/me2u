"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('try.urls')),
    url(r'^login/$', auth_views.login, {'template_name': 'core/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api-token-auth/', obtain_jwt_token),
]

'''
curl - X POST - d "username=aimethierry&password=mamanb123" http://127.0.0.1:8000/api-token-auth/

curl -X POST -H "Content-Type: application/json" -d '{"username":"aimethierry","password":"mamanb123"}' http://localhost:8000/api-token-auth/


{"token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFpbWV0aGllcnJ5IiwidXNlcl9pZCI6MSwiZW1haWwiOiIiLCJleHAiOjE1MTUxMDY1OTZ9.D5RU_pXBrM-TZ-QabJLmt2dl0pxaKCZs743k0d3sPAw"}
'''
