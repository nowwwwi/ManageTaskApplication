from django.urls import path
from .views import IndexView, WorkDetailView, HistoryCreateView

app_name = "houseworks"
urlpatterns = [
    # ex: /houseworks/
    path("", IndexView.as_view(), name="index"),
    # ex: /houseworks/pk/
    path("<int:pk>/", WorkDetailView.as_view(), name="detail"),
    # ex: /create/
    path("create/", HistoryCreateView.as_view(), name="create_history"),
]
