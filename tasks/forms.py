from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    deadline = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'date'}),
        required=False
    )

    class Meta:
        model = Task
        fields = "__all__"
