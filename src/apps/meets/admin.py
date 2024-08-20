from django.contrib import admin

from .models import Category, Meet, MeetParticipant


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)


@admin.register(Meet)
class MeetAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'start_date', 'start_time')
    list_display_links = ('title', 'category', 'start_time')
    search_fields = ('title', 'category', 'start_time', 'end_time')


@admin.register(MeetParticipant)
class MeetParticipantAdmin(admin.ModelAdmin):
    list_display = ('user', 'meet')
    list_display_links = ('user', 'meet')
    search_fields = ('user', 'meet')

