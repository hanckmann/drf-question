# snippets/serializers
from rest_framework import serializers
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos',
                  'language', 'style')
                  # 'language', 'style', 'url')

        # extra_kwargs = {
        #     "url": {"view_name": "snippet-detail", "lookup_field": "pk"},
        # }