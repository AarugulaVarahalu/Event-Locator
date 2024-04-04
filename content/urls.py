from django.urls import path

from .views import Event_details, create_event, update_event,delete_event,view_events,upload_file,search_events

urlpatterns = [
    path('', Event_details, name="Events"),
    path('create_event/', create_event, name="create"),
    path('update_event/<int:id>', update_event, name="update"),
    path('delete_event/<int:id>', delete_event, name="delete"),
    path('view_events/<int:id>', view_events, name="view"),
    path('upload/', upload_file, name='upload_file'),
    path('search/', search_events, name='search_events'),
]