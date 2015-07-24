from django.db import models

from django.utils import timezone

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return '<Client: {}>'.format(self.name)

    
class Project(models.Model):
    name = models.CharField(max_length=200)
    client = models.ForeignKey(Client)

    def __str__(self):
        return '<Project: {} for {}'.format(self.name, self.client.name)


class Entry(models.Model):
    project = models.ForeignKey('Project')
    description = models.CharField(max_length=200)
    start = models.DateTimeField(default=timezone.now)
    stop = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        t = self.start
        from_str = " from {}".format(t) if t else ""
        t = self.stop
        to_str = " to {}".format(t) if t else ""
        if from_str or to_str:
            return '<Entry: For {} {} {}: {}>'.format(self.project.name, from_str, to_str, self.description)
        else:
            return '<Entry: For {} with no times: {}>'.format(self.project.name, self.description)

    def is_finished(self):
        return self.stop is not None
