from django.contrib import admin
from .models import ContactMessage, Technology

# Register your models here.
class ContactMessageAdmin(admin.ModelAdmin):
    readonly_fields = ()

class TechnologyAdmin(admin.ModelAdmin):
    readonly_fields = ('name', 'created')

admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(Technology, TechnologyAdmin)
