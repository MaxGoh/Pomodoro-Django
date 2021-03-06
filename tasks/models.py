from django.db import models
from django.utils.text import slugify
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.conf import settings

class Task(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    id = models.AutoField(primary_key=True)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)  # set the slug explicitly
        super(Task, self).save(*args, **kwargs)  # call Django's save()


class Note(models.Model):
    task = models.ForeignKey(Task)
    name = models.CharField(max_length=50)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    url = models.URLField(blank=True)
    id = models.AutoField(primary_key=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.note


class Duration(models.Model):
    task = models.ForeignKey(Task)
    total_second = models.IntegerField(blank=True);
    started_at = models.TimeField(auto_now_add=True, blank=True, null=True)
    end_at = models.TimeField(auto_now_add=True, blank=True, null=True)

