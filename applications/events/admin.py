from django.contrib import admin

from applications.events.models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "author", "date", "created")
    list_filter = ("created", "author")
    search_fields = ("title", "description")
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ("author",)
    date_hierarchy = "created"
    ordering = ("date",)
