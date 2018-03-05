# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
	list_display = 'email', 'get_creation_date', 'id'

