from django.contrib import admin

from accounts.models import Category
from accounts.models import Info
# Register your models here.

admin.site.register(Category)
admin.site.register(Info)