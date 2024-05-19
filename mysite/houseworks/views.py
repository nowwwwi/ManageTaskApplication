from django.contrib import messages
from django.db.models.query import QuerySet
from django.shortcuts import resolve_url
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Work, History, WorkProcess, HashTag, IntervalType
from .forms import HistoryForm, WorkForm

REDIRECT_PATH = "houseworks:work_list"

# Create your views here.
class WorkModelViews():
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
        success_url = reverse_lazy(REDIRECT_PATH)

        def get_success_url(self):
            messages.success(self.request, "タスクを追加しました")
            return resolve_url(REDIRECT_PATH)


    class WorkUpdateView(UpdateView):
        """"""
        model = Work
        fields = ('name', 'description', 'default_executor','hashtags', 'interval_types')
        template_name_suffix = "_update_form"
        success_url = reverse_lazy(REDIRECT_PATH)

        def get_success_url(self):
            messages.success(self.request, "タスクを更新しました")
            return resolve_url(REDIRECT_PATH)


    class WorkDeleteView(DeleteView):
        model = Work
        success_url = reverse_lazy(REDIRECT_PATH)

        def get_success_url(self):
            messages.success(self.request, "タスクを消去しました")
            return resolve_url(REDIRECT_PATH)

class HistoryModelViews():
    class HistoryListView(ListView):
        model = History


class HashtagModelViews():
    class HashtagListView(ListView):
        model = HashTag
    
    class HashtagCreateView(CreateView):
        model = HashTag


class IntervalModelViews():
    class IntervalListView(ListView):
        model = IntervalType
    

    class IntervalCreateView(CreateView):
        model = IntervalType


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
