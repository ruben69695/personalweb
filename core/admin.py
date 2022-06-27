from django.contrib import admin
from .models import ContactMessage, Technology, BlacklistedWord

# Register your models here.
class ContactMessageAdmin(admin.ModelAdmin):
    readonly_fields = ()

class TechnologyAdmin(admin.ModelAdmin):
    readonly_fields = ['created']

    def get_readonly_fields(self, request, obj=None):
        defaults = super().get_readonly_fields(request, obj=obj)
        if obj:  # if we are updating an object
            defaults = ['name'] + defaults
        return defaults

class BlacklistedWordAdmin(admin.ModelAdmin):
    readonly_fields = ['created']

    def get_readonly_fields(self, request, obj=None):
        defaults = super().get_readonly_fields(request, obj=obj)
        if obj:  # if we are updating an object
            defaults = ['word'] + defaults
        return defaults



admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(Technology, TechnologyAdmin)
admin.site.register(BlacklistedWord, BlacklistedWordAdmin)
