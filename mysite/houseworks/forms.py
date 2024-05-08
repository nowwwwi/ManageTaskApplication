from django import forms
from .models import History, Work


class WorkForm(forms.ModelForm):
    """Form for work"""
    class Meta:
        model = Work
        fields = ('name', 'description', 'hashtags', 'interval_types')
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
            field.widget.attrs['placeholder'] = field.label


class HistoryForm(forms.ModelForm):
    """Form for History."""
    class Meta:
        """Meta data."""
        model = History
        fields = ('user', 'work')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
            field.widget.attrs['placeholder'] = field.label
