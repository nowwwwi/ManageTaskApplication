from django.contrib import messages
from django.shortcuts import resolve_url
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Work, History
from .forms import HistoryForm

# Create your views here.

class IndexView(ListView):
    """
    """
    model = Work
    template_name = "houseworks/index.html"


class WorkDetailView(DetailView):
    """
    """
    model = Work
    template_name = "houseworks/detail.html"


class HistoryCreateView(CreateView):
    model = History
    form_class = HistoryForm
    success_url = reverse_lazy("houseworks:index")

    def get_success_url(self):
        messages.success(self.request, "実行履歴を追加しました")
        return resolve_url("houseworks:index")
