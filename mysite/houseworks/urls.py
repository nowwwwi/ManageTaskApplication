from django.urls import path
from . import views

app_name = "houseworks"
urlpatterns = [
    # ex: /houseworks/
    path("", views.IndexView.as_view(), name="index"),
    # ex: /work/list
    path("work/list", views.WorkListView.as_view(), name="work_list"),
    # ex: /houseworks/pk/
    path("history/specifics/<int:pk>/", views.HistoryDetailView.as_view(), name="history_detail"),
    # ex: /create/
    path("history/create/", views.HistoryCreateView.as_view(), name="history_create"),
]
