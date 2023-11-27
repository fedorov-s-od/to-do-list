from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Task, Tag


class TaskTagViewTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="admin.user",
            first_name="Admin",
            last_name="User",
            password="1qazcde3",
        )
        self.client.force_login(self.user)

        self.tag1 = Tag.objects.create(name="Tag 1")
        self.tag2 = Tag.objects.create(name="Tag 2")
        self.task = Task.objects.create(content="Test Task", created_at="2023-11-27 12:00:00", deadline="2023-12-01 12:00:00")
        self.task.tags.add(self.tag1)

    def test_task_list_view(self):
        response = self.client.get(reverse("tasks:index"))
        self.assertEqual(response.status_code, 200)

    def test_task_create_view(self):
        response = self.client.post(
            reverse("tasks:task-create"),
            {
                "content": "New Test Task",
                "deadline": "12/01/2023",
                "tags": [self.tag1.pk, self.tag2.pk],
            },
        )
        self.assertEqual(response.status_code, 302)

    def test_task_update_view(self):
        response = self.client.post(
            reverse("tasks:task-update", kwargs={"pk": self.task.pk}),
            {
                "content": "Updated Test Task",
                "deadline": "12/02/2023",
                "tags": [self.tag2.pk],
            },
        )
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertEqual(self.task.content, "Updated Test Task")
        self.assertEqual(list(self.task.tags.all()), [self.tag2])

    def test_task_delete_view(self):
        response = self.client.post(reverse("tasks:task-delete", kwargs={"pk": self.task.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(pk=self.task.pk).exists())

    def test_task_change_status_view(self):
        response = self.client.get(reverse("tasks:task-change-status", kwargs={"pk": self.task.pk}))
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertTrue(self.task.is_done)

    def test_tag_list_view(self):
        response = self.client.get(reverse("tasks:tag-list"))
        self.assertEqual(response.status_code, 200)

    def test_tag_create_view(self):
        response = self.client.post(
            reverse("tasks:tag-create"),
            {
                "name": "New Test Tag",
            },
        )
        self.assertEqual(response.status_code, 302)

    def test_tag_update_view(self):
        response = self.client.post(
            reverse("tasks:tag-update", kwargs={"pk": self.tag1.pk}),
            {
                "name": "Updated Test Tag",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.tag1.refresh_from_db()
        self.assertEqual(self.tag1.name, "Updated Test Tag")

    def test_tag_delete_view(self):
        response = self.client.post(reverse("tasks:tag-delete", kwargs={"pk": self.tag2.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Tag.objects.filter(pk=self.tag2.pk).exists())
