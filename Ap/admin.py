from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

from .models import Post, Comment


admin.site.register(Post)
admin.site.register(Comment)
