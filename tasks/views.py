from django.shortcuts import render
from django.views import generic

from .models import Task, Tag


def index(request):
    """View function for the home page of the site."""

    return render(request, "tasks/index.html", context={})


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "tasks/tag_list.html"
    paginate_by = 5
