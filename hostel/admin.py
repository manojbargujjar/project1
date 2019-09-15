# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import User,Room,Complain

admin.site.register(User)
admin.site.register(Room)
admin.site.register(Complain)

# Register your models here.
