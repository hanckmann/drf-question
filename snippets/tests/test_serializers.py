from django.db.models.signals import post_save
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.request import Request

from django.test import TestCase
from rest_framework.test import APIClient, APIRequestFactory
import factory

from accounts.tests.factories import UserFactory
from snippets.serializers import SnippetSerializer
from snippets.models import Snippet


SNIPPETS_URL = reverse('snippet-list')


class TestSnippetSerializer(TestCase):

    @factory.django.mute_signals(post_save)
    def setUp(self):
        self.user = UserFactory(email="user@example.com")
        self.client = APIClient()
        self.client.force_authenticate(self.user)
        factory = APIRequestFactory()
        request = factory.get('/')
        self.serializer_context = {
            'request': Request(request),
        }

    @factory.django.mute_signals(post_save)
    def test_retrieve_snippet_list(self):
        Snippet.objects.create(title='snip 1', owner=self.user)
        Snippet.objects.create(title='snip 2', code='some code;', owner=self.user)
        Snippet.objects.create(title='snip 3', code='more code;', language='Python', owner=self.user)
        result = self.client.get(SNIPPETS_URL)
        snippets = Snippet.objects.all().order_by('id')
        serializer = SnippetSerializer(snippets, context=self.serializer_context, many=True)
        print(snippets)
        print(result.data)
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        self.assertEqual(result.data['results'], serializer.data)

    @factory.django.mute_signals(post_save)
    def test_create_snippet_successful(self):
        payload = {
            'title': 'test snippet',
            'code': 'source code;',
            'language': 'python'
        }
        ret = self.client.post(SNIPPETS_URL, payload)
        exists = Snippet.objects.filter(
            title=payload['title'],
        ).exists()
        snippets = Snippet.objects.filter(
            title=payload['title'],
        ).all()
        print(ret)
        self.assertEqual(ret.status_code, status.HTTP_201_CREATED)
        self.assertTrue(exists)
        self.assertEqual(len(snippets), 1)
        self.assertEqual(snippets[0].title, payload['title'])
        self.assertEqual(snippets[0].code, payload['code'])
        self.assertEqual(snippets[0].language, payload['language'])
        self.assertEqual(snippets[0].owner, self.user)
