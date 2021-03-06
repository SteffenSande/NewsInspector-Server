from django.db import models

from headlineScraper.models.diff import Diff


class Change(models.Model):
    """ A model that contains one change in the text that is stored in the diff object"""

    diff = models.ForeignKey(Diff, on_delete=models.CASCADE)
    text = models.TextField(default=None, null=True)
    type_of_change = models.IntegerField(default=None, null=True)
    pos = models.IntegerField(default=None, null=True)
    title = models.BooleanField(default=False, null=False)

    class Meta:
        ordering = ('pos',)
