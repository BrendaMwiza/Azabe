# -*- coding: utf-8 -*-



# from __future__ import unicode_literals

from django.contrib import admin
from .models import Post, Parents, Child, Partners, Activities



# Register your models here.
admin.site.register(Parents)
admin.site.register(Partners)
admin.site.register(Post)
admin.site.register(Activities)



#create a Admin_site object to register models
# admin_site = CustomLoginAdminSite()

# #register Models as usual
# admin_site.register(MyModel)
