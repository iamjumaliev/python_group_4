from accounts.models import UserProfile
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User




class ProfileInline(admin.StackedInline):
    model = UserProfile
    fields = ['avatar','about']


class UserProfileAdmin(UserAdmin):
    inlines = [ProfileInline]


admin.site.unregister(User)
admin.site.register(User, UserProfileAdmin)
# Register your models here.
