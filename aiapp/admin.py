from django.contrib import admin
from .models import FeedBack
# Register your models here.

class FeedBackAdmin(admin.ModelAdmin):
    list_display = ('user', 'feedback', 'date')
    list_filter = ('user', 'date')
    search_fields = ('user__username', 'feedback')
    date_hierarchy = 'date'
    ordering = ('-date',)

    fieldsets = (
        ('User Information', {'fields': ('user',)}),
        ('Feedback Details', {'fields': ('feedback',)}),
        ('Date Information', {'fields': ('date',)}),
    )
    readonly_fields = ('date',)

admin.site.register(FeedBack, FeedBackAdmin)