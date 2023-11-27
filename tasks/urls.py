from django.urls import path

from .views import (
    index,
    TagListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    task_change_status
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "tags/",
        TagListView.as_view(),
        name="tag-list",
    ),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path(
        "tasks/<int:pk>/taskchangestatus/",
        task_change_status,
        name="task-change-status",
    ),
]

app_name = "tasks"
