from django.contrib import admin

from .models import video
from .models import video2
# Register your models here.
@admin.register(video)
class UserAdmin(admin.ModelAdmin):
    list_display = ('video1','video2',)

@admin.register(video2)
class UserAdmin(admin.ModelAdmin):
    list_display = ('image','video3',)