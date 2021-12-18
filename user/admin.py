from django.contrib import admin
from user.models import UserOTP, Profile, Notification

# Register your models here.
admin.site.register(UserOTP)
admin.site.register(Profile)
admin.site.register(Notification)
