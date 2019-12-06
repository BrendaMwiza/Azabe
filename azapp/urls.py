from django.conf.urls import url,include
from . import views
# from django.conf import settings
# from django.conf.urls.static import static
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^new/post$',views.new_post, name ='new-post'),
    url(r'^new/newchild$',views.new_child, name ='new-child'),
    url(r'^new/child$',views.child, name ='child'),
    url(r'^partners/$',views.partners,name = 'partner'),
    url(r'^new_event/$',views.new_event,name = 'event'),
    url(r'^subscribers/(\d+)',views.subscribers,name = 'sub'),
    url(r'^myprofile/$',  views.profilemy,name='profilemy'),
    url(r'^editprofile',views.editProfile, name='editProfile'),
    url(r'^dashboard/', views.dashboard, name='dash'),
    url(r'^profile/', views.getProfile, name='profile'),
    url(r'^parprofile/', views.pargetProfile, name='parprofile'),
    
    url(r'^pareditprofile',views.username_present, name='username_present'),
   
    url(r'^new/comment/(\d+)/$',views.comment, name ='comment'),
    url(r'^activity/(\d+)/$',views.activity, name ='activity'),
  
    url(r'^new/blog$',views.new_blog, name ='new-blog'),
    url(r'^blog$',views.blog, name ='blog'),
    url(r'^activity/(\d+)$',views.activity, name ='activity'),
    url(r'^likes/(?P<id>\d+)',views.likes, name="like"),
    url(r'^new/commentblog/(\d+)/$',views.commentblog, name ='commentblog'),
  
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
