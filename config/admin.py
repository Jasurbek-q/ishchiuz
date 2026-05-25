from django.contrib import admin
from .models import Ishchi

@admin.register(Ishchi)
class IshchiAdmin(admin.ModelAdmin):
    list_display  = ('name', 'surname', 'sohasi', 'age', 'created_at')
    search_fields = ('name', 'surname', 'sohasi')
    list_filter   = ('sohasi',)