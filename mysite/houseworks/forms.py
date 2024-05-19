from django import forms
from .models import History, Work, WorkSchedule


class WorkForm(forms.ModelForm):
    """Form for work"""
    class Meta:
        model = Work
        fields = (
            'name',
            'description',
            'default_executor',
            'next_execute_date',)

        widgets = {
            'description': forms.Textarea(attrs={'type': 'str'}),
            'next_execute_date': forms.DateInput(attrs={'type': 'date'})
        }

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
        fields = (
            'user',
            'work')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
            field.widget.attrs['placeholder'] = field.label


class WorkScheduleForm(forms.ModelForm):
    class Meta:
        model = WorkSchedule
        fields = (
            "work",
            "schedule",
        )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
            field.widget.attrs['placeholder'] = field.label
