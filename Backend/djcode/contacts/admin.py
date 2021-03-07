from django.contrib import admin
from .models import CallBack


@admin.register(CallBack)
class CallBackAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'complete', 'service', 'date', 'update')
    list_editable = ('complete',)
    list_filter = ('complete', 'service', 'date', 'update')
    search_fields = ('phone', 'name')
