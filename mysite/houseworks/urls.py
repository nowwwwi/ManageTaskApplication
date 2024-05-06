from django.urls import path
from . import views

app_name = "houseworks"
urlpatterns = [
    # ex: /houseworks/
    path("", views.IndexView.as_view(), name="index"),
    # ex: /work/list
    path("work/list", views.WorkListView.as_view(), name="work_list"),
    # ex: /work/specifics/13/
    path("work/specifics/<int:pk>/", views.WorkDetailView.as_view(), name="work_detail"),
    # ex: /houseworks/4/
    path("history/specifics/<int:pk>/", views.HistoryDetailView.as_view(), name="history_detail"),
    # ex: /create/
    path("history/create/", views.HistoryCreateView.as_view(), name="history_create"),
]
