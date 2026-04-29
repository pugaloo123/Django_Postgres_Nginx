from django.contrib import admin
from .models import Athlete


@admin.register(Athlete)
class AthleteAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'created_at')
    search_fields = ('name',)
    list_filter = ('age',)
