# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http  import HttpResponse, Http404, HttpResponseRedirect
from .models import Post, Parents, Child, Partners, Activities
from .forms import NewPostForm, RegChildForm,ActivityForm,UpdateProForm
# Create your views here.
# @login_required(login_url='/accounts/login/')

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


@login_required(login_url='/accounts/login/')
def getProfile(request,users=None):
    user = request.user
    image = Parents.objects.filter(name=user)
    name = request.user
    profile = Parents.objects.filter(name=name).all()
    
    return render(request,'profile/profile.html',locals(),{"image":image})


@login_required(login_url='/accounts/login/')
def editProfile(request):
    current_user = request.user
    if request.method == 'POST':
        form = UpdateProForm(request.POST,request.FILES)
        if form.is_valid():
            pics = form.save(commit=False)
            pics.user_name = current_user
            pics.save()
        return redirect('profile')

    else:
        form = UpdateProForm()
    return render(request,'profile/editProfile.html',{"test":form})


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




# @login_required(login_url='/accounts/login/')
def new_event(request):
    current_user = request.user

    if request.method == 'POST':
        form = ActivityForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = current_user
            event.save()
        return redirect('partner')
    else:
        form = ActivityForm()
    return render(request, 'new_event.html', {"form": form})


def subscribers(request,act_id):
    act = Activities.objects.filter(id=act_id).first()
    print(act)
    child = Child.objects.filter(activity_id=act.id)
    return render(request, 'subscribers.html', {"child": child,"act":act})



def dashboard(request):
    current_user = request.user
    activities = Activities.objects.all()
    return render(request,'events.html',{ 'current_user':current_user, 'activities':activities})


# @login_required(login_url='/accounts/login/')
def partners(request):
    current_user = request.user
    # even = Activities.objects.filter(=even_id).first()
    
    act = Activities.objects.filter(partner_name=current_user.id).all()
    return render(request, 'partners.html', {"act":act})


