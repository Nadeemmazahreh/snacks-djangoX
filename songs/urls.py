from django.urls import path
from .views import (
    SongListView,
    SongCreateView,
    SongDeleteView,
    SongDetailView,
    SongListView,
    SongUpdateView,
)

urlpatterns = [
    path('', SongListView.as_view(), name='song-list'),
    path("<int:pk>/", SongDetailView.as_view(), name="song-detail"),
    path("create/", SongCreateView.as_view(), name="song-create"),
    path("<int:pk>/update/", SongUpdateView.as_view(), name="song-update"),
    path("<int:pk>/delete/", SongDeleteView.as_view(), name="song-delete")
]