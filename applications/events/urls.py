from django.urls import path

from applications.events import views

app_name = "events"

urlpatterns = [
    path("", views.event_list, name="event_list"),
    path("add_event/", views.add_event, name="add_event"),
    path("edit_event/<slug:event>/", views.edit_event, name="edit_event"),
    path("delete_event/<slug:event>", views.delete_event, name="delete_event"),
    path("<slug:event>/", views.event_detail, name="event_detail"),
    path("search/", views.event_search, name="event_search"),
]
