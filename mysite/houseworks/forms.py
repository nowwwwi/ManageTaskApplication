from django import forms
from .models import History


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
