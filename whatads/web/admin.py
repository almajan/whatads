from django.contrib import admin
from .models import SendMsg, SendImg, SendVdo, SendVce, CheckDlvy, CheckSeen, Token

# Register your models here.
admin.site.register(SendMsg)
admin.site.register(SendImg)
admin.site.register(SendVdo)
admin.site.register(SendVce)
admin.site.register(CheckDlvy)
admin.site.register(CheckSeen)
admin.site.register(Token)
