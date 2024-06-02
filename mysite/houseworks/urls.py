from django.urls import path
from . import views
from .views import IndexView, WorkModelViews, HistoryModelViews

app_name = "houseworks"
urlpatterns = [
    # ex: /houseworks/
    path("", IndexView.as_view(), name="index"),
    # ex: /work/list
    path("work/list", WorkModelViews.WorkListView.as_view(), name="work_list"),
    # ex: /work/create
    path("work/create", WorkModelViews.WorkCreateView.as_view(), name="work_create"),
    # ex: /work/specifics/13/
    path("work/specifics/<int:pk>/", WorkModelViews.WorkDetailView.as_view(), name="work_detail"),
    # ex: /work/update/4/
    path("work/update/<int:pk>/", WorkModelViews.WorkUpdateView.as_view(), name="work_update"),
    # ex: /houseworks/delete/4/
    path("work/delete/<int:pk>", WorkModelViews.WorkDeleteView.as_view(), name="work_delete"),
    # ex: /history/list
    path("history/list", HistoryModelViews.HistoryListView.as_view(), name="history_list"),
    # ex:
    path("history/specifics/<int:pk>/", views.HistoryDetailView.as_view(), name="history_detail"),
    # ex: /history/create/
    path("history/create/", views.HistoryCreateView.as_view(), name="history_create"),
    path("workschedule/create/", views.WorkScheduleCreateView.as_view(), name="workschedule_create"),
]
