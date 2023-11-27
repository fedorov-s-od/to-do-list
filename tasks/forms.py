from datetime import datetime

from django import forms

from .models import Task


class DateTimeWidget(forms.MultiWidget):
    def __init__(self, attrs=None):
        date_attrs = {'type': 'date'}
        time_attrs = {'type': 'time'}
        if attrs:
            date_attrs.update(attrs)
            time_attrs.update(attrs)

        widgets = (forms.DateInput(attrs=date_attrs), forms.TimeInput(attrs=time_attrs, format='%H:%M'))
        super().__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return [value.date(), value.time()]
        return [None, None]

    def value_from_datadict(self, data, files, name):
        date_value = self.widgets[0].value_from_datadict(data, files, f'{name}_0')
        time_value = self.widgets[1].value_from_datadict(data, files, f'{name}_1')
        if date_value and time_value:
            full_date_time = f'{date_value} {time_value}'
            return datetime.strptime(full_date_time, '%Y-%m-%d %H:%M')
        return None

    def format_output(self, rendered_widgets):
        return '<div class="datetime-widget">{}</div>'.format(' '.join(rendered_widgets))


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = "__all__"

        widgets = {
            'deadline': DateTimeWidget
        }
