from django.contrib import admin
from .models import File


class FileAdmin(admin.ModelAdmin):
    list_display = ('file', 'processed')
    list_filter = ('processed',)


admin.site.register(File, FileAdmin)
