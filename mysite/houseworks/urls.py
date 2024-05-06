from django.urls import path
from .views import IndexView, HistoryDetailView, HistoryCreateView

app_name = "houseworks"
urlpatterns = [
    # ex: /houseworks/
    path("", IndexView.as_view(), name="index"),
    # ex: /houseworks/pk/
    path("history/specifics/<int:pk>/", HistoryDetailView.as_view(), name="history_detail"),
    # ex: /create/
    path("history/create/", HistoryCreateView.as_view(), name="history_create"),
]
