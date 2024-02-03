from django.contrib import admin
from .models import File


class FileAdmin(admin.ModelAdmin):
    list_display = ('file', 'uploaded_date', 'processed')
    list_filter = ('uploaded_date', 'processed')


admin.site.register(File, FileAdmin)
