from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from .models import Task, Tag
from .forms import TaskForm


class TaskListView(LoginRequiredMixin, generic.ListView):
    template_name = "tasks/index.html"
    context_object_name = "task_list"
    paginate_by = 5

    def get_queryset(self):
        return Task.objects.all().order_by('is_done', '-created_at').prefetch_related('tags')


class TagListView(LoginRequiredMixin, generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "tasks/tag_list.html"
    paginate_by = 5


class TagCreateView(LoginRequiredMixin, generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks:tag-list")


class TagUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks:tag-list")


class TagDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("tasks:tag-list")


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:index")


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:index")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:index")


@login_required
def task_change_status(request, pk):
    task = Task.objects.get(id=pk)
    if task.is_done:
        task.is_done = False
    else:
        task.is_done = True
    task.save()
    return HttpResponseRedirect(reverse_lazy("tasks:index"))
