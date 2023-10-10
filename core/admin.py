from django.contrib import admin

from authentication.models import MyUser
from blog.models import Blog

# Register your models here.

admin.site.register(MyUser)
admin.site.register(Blog)