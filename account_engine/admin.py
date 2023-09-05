from django.contrib import admin
from .models import User, UserMeta

admin.site.register(User)
admin.site.register(UserMeta)
