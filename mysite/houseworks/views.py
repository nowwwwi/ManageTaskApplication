from django.contrib import messages
from django.shortcuts import resolve_url
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Work, History, WorkProcess, WorkSchedule
from .forms import HistoryForm, WorkForm

REDIRECT_PATH = "houseworks:work_list"


# Create your views here.
class IndexView(ListView):
    """View for index '/' """
    model = Work
    template_name = "houseworks/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task_count"] = Work.objects.all().count
        context["history_count"] = History.objects.all().count
        return context


class WorkModelViews():
    class WorkListView(ListView):
        model = Work

    class WorkDetailView(DetailView):
        """"""
        model = Work

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context["work_processes"] = WorkProcess.objects.filter(work=self.object)
            context["work_schedules"] = WorkSchedule.objects.filter(work=self.object)
            context["histories"] = History.objects.filter(work=self.object)
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
        form_class = WorkForm
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


class HistoryDetailView(DetailView):
    """View for detail '/specifics/<int:pk>'"""
    model = History
    template_name = "houseworks/detail.html"


class HistoryCreateView(CreateView):
    model = History
    form_class = HistoryForm
    success_url = reverse_lazy("houseworks:history_list")

    def get_initial(self):
        initial = super().get_initial()
        initial['user'] = self.request.GET.get('user', '')
        initial['work'] = self.request.GET.get('work', '')
        return initial

    def get_success_url(self):
        messages.success(self.request, "実行履歴を追加しました")
        return resolve_url("houseworks:history_list")
