from django.contrib import admin
from .models import SendMsg, SendImg, SendVdo, SendVce

# Register your models here.
admin.site.register(SendMsg)
admin.site.register(SendImg)
admin.site.register(SendVdo)
admin.site.register(SendVce)
