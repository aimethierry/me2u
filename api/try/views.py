# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import MyModelForm, SignUpForm
from .models import compony, users
from rest_framework.response import Response
from rest_framework import generics
from .serializers import ComponylistSerializer, UserlistSerializer, ClientSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions

from django.contrib.auth.models import User

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


def aime(request):
    return HttpResponse("hello aime")


# for api
class ComponyCreateAPIView(generics.ListCreateAPIView):
    queryset = users.objects.all()
    serializer_class = ComponylistSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserlistSerializer
    permission_classes = [permissions.IsAuthenticated]


class ClientCreateAPIView(generics.ListAPIView):
    queryset = compony.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]


#for list api
class ComponyListAPIView(generics.ListAPIView):
    queryset = users.objects.all()
    serializer_class = ComponylistSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserlistSerializer
    permission_classes = [permissions.IsAuthenticated]


class ClientListAPIView(generics.ListAPIView):
    queryset = compony.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]

    


#for details
class ComponyADetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = users.objects.all()
    serializer_class = ComponylistSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserADetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserlistSerializer




#for deleting

class UserDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserlistSerializer


class ComponyDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = users.objects.all()
    serializer_class = ComponylistSerializer


    



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def home(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MyModelForm()
    
        return render(request, 'create.html')


def create(request):
        if request.method == 'POST':
            name = request.POST['name'],
            title = request.POST['title'],

            compony.objects.create(
                name = name,
                title = title,
            )
        return HttpResponse("created")


def list(request):
    name = compony.objects.all()
    context = {
    "name":name
    }
    return render(request, 'list.html', context)



'''
def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TweetCreateView, self).form_valid(form)
'''

#
# def list(request):
#     name = Titi.objects.all()
#
#     answer_data = {
#     "answer_detail" : answer_info
#     }
#
# print answer_data
#  return render_to_response('quizzes.html'', answer_data, context_instance=RequestContext(request))
