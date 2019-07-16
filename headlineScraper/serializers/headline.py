from rest_framework import serializers
from headlineScraper.models import HeadlineRevision
from headlineScraper.serializers.diff import DiffSerializer
from headlineScraper.models import HeadlineTemplate, Rank, Headline


class HeadlineRevisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeadlineRevision
        exclude = ('headline', 'id')


class HeadlineTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeadlineTemplate
        exclude = ('created', 'modified', 'id')


class RankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rank
        exclude = ('headline', 'modified',)


class HeadlineSerializer(serializers.ModelSerializer):
    ranks = RankSerializer(many=True, read_only=True)
    revisions = HeadlineRevisionSerializer(many=True)
    # summary = HeadlineSummarySerializer()
    # reports = serializers.SerializerMethodField()
    # info = serializers.SerializerMethodField()
    # revision = HeadlineRevisionSerializer()
    diffs = DiffSerializer(many=True)

    class Meta:
        model = Headline
        exclude = ('created',)

    #def get_info(self, obj):
    #    from articleScraper.models import Article
    #    try:
    #        info = Article.objects.get(headline=obj)
    #        return ArticleInfoForHeadlineSerializer(info).data
    #    except Article.DoesNotExist:
    #        return None

    #def get_reports(self, obj):
    #    from submission.models import Report
    #    report = Report.objects.filter(headline=obj)
    #    return ReportSerializer(report, many=True).data



class HeadlineListSerializer(serializers.ModelSerializer):
    # reports = serializers.SerializerMethodField()
    # info = serializers.SerializerMethodField()
    # revision = HeadlineRevisionSerializer()
    revisions = HeadlineRevisionSerializer(many=True)
    diffs = DiffSerializer(many=True)

    class Meta:
        model = Headline
        exclude = ('created',)

    #def get_info(self, obj):
    #    from articleScraper.models import Article
    #    try:
    #        info = Article.objects.get(headline=obj)
    #        return ArticleInfoForHeadlineSerializer(info).data
    #    except Article.DoesNotExist:
    ##        return None

    #def get_reports(self, obj):
    #    from submission.models import Report
    #    report = Report.objects.filter(headline=obj)
    #    return ReportSerializer(report, many=True).data
#
#    def get_diffs(serializer, self):
#        from differ.diff import Differ
#        revisions = list(self.revisions)
#        revisions.sort(key=lambda rev: rev.version, reverse=True)
#        diffs = [(revisions[0].title, revisions[0].sub_title)]

#        for index, revision in enumerate(revisions[1:]):
#            # index will be one less then we expect because I split the list from the 1st element.
#            title_diff = Differ(revisions[index].title,  revision.title)
#            sub_title_diff = Differ(revisions[index].sub_title,  revision.sub_title)
#            if title_diff.is_diff or sub_title_diff.is_diff:
#                diffs.append((title_diff.diff, sub_title_diff.diff))
#        return diffs
