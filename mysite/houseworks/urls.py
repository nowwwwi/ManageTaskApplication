from django.urls import path
from . import views
from .views import WorkModelViews, HistoryModelViews, HashtagModelViews, IntervalModelViews

app_name = "houseworks"
urlpatterns = [
    # ex: /houseworks/
    path("", WorkModelViews.IndexView.as_view(), name="index"),
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
    # ex: /hashtag/list
    path("hashtag/list", HashtagModelViews.HashtagListView.as_view(), name="hashtag_list"),
    # ex: /hashtag/create
    path("hashtag/create", HashtagModelViews.HashtagCreateView.as_view(), name="hashtag_create"),
    # ex: /interval/list
    path("interval/list", IntervalModelViews.IntervalListView.as_view(), name="interval_list"),
    # ex: /interval/create
    path("interval/create", IntervalModelViews.IntervalCreateView.as_view(), name="interval_create"),
]
