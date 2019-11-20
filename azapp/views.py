# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http  import HttpResponse
from django.contrib.auth.models import User

# Create your views here.
# def home_images(request):

#     return render(request,'index.html')
    # return HttpResponse('Welcome to the Moringa Tribune')from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http  import HttpResponse, Http404, HttpResponseRedirect
from .models import Post, Parents, Child, Partners, Activities
from .forms import NewPostForm, RegChildForm,UpdateProForm,UpdateParForm,partnerForm
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
@login_required(login_url='/accounts/login/')
def getProfile(request,users=None):
    user = request.user
    parent_image = Parents.objects.filter(name=user)
    name = request.user
    profile = Parents.objects.filter(name=name).all()
    return render(request,'profile/profile.html',locals(),{"parent_image":parent_image})
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

@login_required(login_url='/accounts/login/')
def pargetProfile(request,users=None):
    user = request.user
    parent_image = Partners.objects.filter(partner_name=user)
    name = request.user
    profile = Partners.objects.filter(partner_name=name).all()
    return render(request,'profile/partner_Profile.html',locals(),{"parent_image":parent_image})

@login_required(login_url='/accounts/login/')
def pareditProfile(request):
    current_user = request.user
    if request.method == 'POST':
        form = UpdateParForm(request.POST,request.FILES)
        if form.is_valid():
            pics = form.save(commit=False)
            pics.user_name = current_user
            pics.save()
        return redirect('parprofile')
    else:
        form = UpdateParForm()
    return render(request,'profile/pareditProfile.html',{"form":form})
# ============================
def username_present(username):
    user=request.user
    partner= Partners.objects.filter(user=user).first()
    if partner.approved == True:
        redirect("partner")
    else:
        form= partnerForm()
    return render (request, 'profile/partn.html', {"form":form})
    
    # partner=Partners.objects.filter(partner_name=user)
    # if User.objects.filter(username=username).exists():
    #     return True
    
    # return False






