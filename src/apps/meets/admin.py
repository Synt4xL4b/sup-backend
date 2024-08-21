from django.contrib import admin

from apps.meets.models import Category, Meet


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_display_links = ("name",)
    search_fields = ("name",)


@admin.register(Meet)
class MeetAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "start_date", "start_time")
    list_display_links = ("title", "category", "start_time")
    search_fields = ("title", "category", "start_time", "end_time")

#
# @admin.register(MeetParticipant)
# class MeetParticipantAdmin(admin.ModelAdmin):
#     list_display = ("user", )
#     list_display_links = ("user", )
#     search_fields = ("user", )

