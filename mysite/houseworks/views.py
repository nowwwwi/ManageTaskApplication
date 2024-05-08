from django.contrib import messages
from django.db.models.query import QuerySet
from django.shortcuts import resolve_url
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Work, History, WorkProcess
from .forms import HistoryForm, WorkForm

# Create your views here.
class IndexView(ListView):
    """View for index '/' """
    model = History
    template_name = "houseworks/index.html"


class WorkListView(ListView):
    model = Work


class WorkDetailView(DetailView):
    """"""
    model = Work
    queryset = Work.objects.prefetch_related(
        "hashtags",
        "interval_types",
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["work_processes"] = WorkProcess.objects.filter(work=self.object)
        return context


class WorkCreateView(CreateView):
    """"""
    model = Work
    form_class = WorkForm
    success_url = reverse_lazy("houseworks:work_create")

    def get_success_url(self):
        messages.success(self.request, "タスクを追加しました")
        return resolve_url("houseworks:work_create")


class HistoryDetailView(DetailView):
    """View for detail '/specifics/<int:pk>'"""
    model = History
    template_name = "houseworks/detail.html"


class HistoryCreateView(CreateView):
    model = History
    form_class = HistoryForm
    success_url = reverse_lazy("houseworks:history_create")

    def get_success_url(self):
        messages.success(self.request, "実行履歴を追加しました")
        return resolve_url("houseworks:history_create")
