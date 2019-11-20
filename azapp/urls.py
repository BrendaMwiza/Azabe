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
    url(r'^subscribers/$',views.subscribers,name = 'sub'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
