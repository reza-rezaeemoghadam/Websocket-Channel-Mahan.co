from django.contrib import admin

from message_app.models import Message, Company
# Register your models here.
admin.site.register(Message)
admin.site.register(Company)