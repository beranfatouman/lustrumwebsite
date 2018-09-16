from django.contrib import admin

# Register your models here.
from .models import posts, Amice

admin.site.register(posts)
admin.site.register(Amice)