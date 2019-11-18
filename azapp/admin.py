# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Trainer, Parents

# Register your models here.
admin.site.register(Parents)
admin.site.register(Trainer)
admin.site.register(Post)