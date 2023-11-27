from django.urls import path

from .views import (
    TagListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagCreateView,
    TagDeleteView,
    TagUpdateView,
    task_change_status, TaskListView
)

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path(
        "tags/",
        TagListView.as_view(),
        name="tag-list",
    ),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    path(
        "tasks/<int:pk>/taskchangestatus/",
        task_change_status,
        name="task-change-status",
    ),
]

app_name = "tasks"
