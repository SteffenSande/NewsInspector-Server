from django import forms
from django.contrib import admin
from django.db import models
from articleScraper.models.article import Article
from helpers.base_models import RevisionBase


class Revision(RevisionBase):
    class Meta:
        ordering = ('version',)

    article = models.ForeignKey(Article, on_delete=models.CASCADE, )
    title = models.TextField()
    sub_title = models.TextField()
    journalists = models.ManyToManyField('articleScraper.Journalist')
    images = models.ManyToManyField('articleScraper.ArticleImage')

    words = models.IntegerField()
    subscription = models.BooleanField(default=False)
    @property
    def diffs(self):
        return self.diff_set.all()

    @property
    def contents(self):
        return self.content_set.all()



class RevisionModelAdminForm(forms.ModelForm):
    journalists = forms.MultipleChoiceField()
    images = forms.MultipleChoiceField()
    url = forms.URLField(disabled=True)

    def __init__(self, *args, **kwargs):
        from articleScraper.models import ArticleImage
        from articleScraper.models import Journalist

        super(RevisionModelAdminForm, self).__init__(*args, **kwargs)
        if 'instance' in kwargs:
            self.fields['images'].choices = [(None, f) for f in
                                             ArticleImage.objects.filter(revision=kwargs['instance'])]
            self.fields['journalists'].choices = [(None, f) for f in
                                                  Journalist.objects.filter(revision=kwargs['instance'])]

            self.fields['url'].initial = kwargs['instance'].article.headline.url

    class Meta:
        model = Revision
        fields = '__all__'


class RevisionAdmin(admin.ModelAdmin):
    readonly_fields = ('title', 'timestamp', 'subscription', 'version')
    search_fields = ('title', 'version',)
    list_display = ['title', 'timestamp', 'version', 'subscription']

    list_filter = [
        'version',
    ]

    form = RevisionModelAdminForm
    exclude = ('images', 'journalists',)


