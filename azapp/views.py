# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http  import HttpResponse, Http404, HttpResponseRedirect
from .models import Post, Parents, Child, Partners, Activities
from .forms import NewPostForm, RegChildForm

def welcome(request):
    post = Post.objects.all()
    child = Child.objects.all()
    partners = Partners.objects.all()
    parent = Parents.objects.all()
    return render(request, 'index.html', {'post':post, 'child':child, 'partners':partners, 'parent':parent})
# login_required(login_url='/accounts/login')
def post(request, id):
    try:
        posts= Post.objects.get(id=id)
    except DoesNotExist:
        raise Http404
    return render(request, 'index.html',{'post':post})

# @login_required(login_url='/accounts/login')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect('welcome')
    else:
        form = NewPostForm()
    return render (request, 'new_post.html', {"form":form})

# @login_required(login_url='/accounts/login')
def child(request):
    current_user = request.user
    child = Child.objects.filter(user=current_user).first()
    return render(request, 'child.html',{'child':child})
# @login_required(login_url='/accounts/login')
def new_child(request):
    current_user = request.user
    if request.method == 'POST':
        form = RegChildForm(request.POST, request.FILES)
        if form.is_valid():
            child = form.save(commit=False)
            child.user = current_user
            child.save()
        return redirect('welcome')
    else:
        form = RegChildForm()
    return render (request, 'new_child.html', {"form":form})
# @login_required(login_url='/accounts/login')
# def Trainer(request):
#     current_user = request.user
#     trainer = Trainer.objects.filter(user=current_user).first()
#     return render(request, 'trainer.html',{'trainer':trainer})
# @login_required(login_url='/accounts/login')
# def new_Trainer(request):
#     current_user = request.user
#     if request.method == 'POST':
#         form = RegTrainerForm(request.POST, request.FILES)
#         if form.is_valid():
#             trainer = form.save(commit=False)
#             trainer.user = current_user
#             trainer.save()
#         return redirect('welcome')
#     else:
#         form = RegTrainerForm()
#     return render (request, 'new_trainer.html', {"form":form})

