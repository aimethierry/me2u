# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import compony, client, users

admin.site.register(compony)
admin.site.register(client)
admin.site.register(users)

