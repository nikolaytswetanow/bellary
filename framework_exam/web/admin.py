from django.contrib import admin

from framework_exam.web.models import AppUser, Photo


@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_staff', 'date_joined')


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
