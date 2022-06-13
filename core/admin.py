from django.contrib import admin
from .models import ContactMessage

# Register your models here.
class ContactMessageAdmin(admin.ModelAdmin):
    readonly_fields = ()


admin.site.register(ContactMessage, ContactMessageAdmin)