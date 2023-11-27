from django.db import models
from django.utils.functional import cached_property


class Task(models.Model):
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField('Tag', related_name='tasks')

    @cached_property
    def tags_to_str(self):
        return ", ".join(self.tags.all().values_list('name', flat=True))

    def __str__(self):
        return self.content


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
