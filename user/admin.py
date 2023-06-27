from django.contrib import admin
from user.models import CustomUser
from user.models import NewsLetter,Message
# class Changedefaultuser(admin.ModelAdmin):
#     list_display = ("username","first_name","last_name","email","number", "kode")

admin.site.register([CustomUser])
admin.site.register([NewsLetter,Message])